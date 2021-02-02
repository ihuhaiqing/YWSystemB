from rest_framework import viewsets,status
from rest_framework.response import Response
from guardian.shortcuts import get_objects_for_user, assign_perm
from django.contrib.auth.models import Group


class CheckPermViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user_groups = Group.objects.filter(user=user)
        if user.has_perm('%s.add_%s' % (app, self.basename)):
            self.perform_create(serializer)
            if not user.is_superuser:
                instance = mdl.objects.get(pk=serializer.data['id'])
                if len(user_groups) == 0:
                    assign_perm('change_%s' % self.basename, instance)
                    assign_perm('view_%s' % self.basename, instance)
                    assign_perm('delete_%s' % self.basename, instance)
                else:
                    for user_group in user_groups:
                        assign_perm('change_%s' % self.basename, user_group, instance)
                        assign_perm('view_%s' % self.basename, user_group, instance)
                        assign_perm('delete_%s' % self.basename, user_group, instance)
        else:
            return Response(data='没有新增权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        queryset = get_objects_for_user(request.user, '%s.view_%s' %(app, self.basename))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        instance = self.get_object()
        user = request.user
        if user.has_perm('view_%s' % self.basename,instance) or user.has_perm('%s.view_%s' % (app,self.basename)):
            serializer = self.get_serializer(instance)
        else:
            return Response(data='没有查看权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if user.has_perm('change_%s' % self.basename, instance) or user.has_perm('%s.update_%s' % (app,self.basename)):
            self.perform_update(serializer)
        else:
            return Response(data='没有编辑权限，请联系管理员添加权限！',status=status.HTTP_403_FORBIDDEN)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        instance = self.get_object()
        user = request.user
        if user.has_perm('delete_%s' % self.basename, instance) or user.has_perm('%s.delete_%s' % (app,self.basename)):
            self.perform_destroy(instance)
        else:
            return Response(data='没有删除权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_204_NO_CONTENT)
