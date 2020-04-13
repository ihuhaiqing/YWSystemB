from django.contrib.auth.models import User, Group, ContentType
from rest_framework import viewsets,status
from app.drf.serializers.auth import UserSerializer, GetUserSerializer,GroupSerializer, GetGroupSerializer, ContentTypeSerializer
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from app.drf.viewsets import CheckPermViewSet
from guardian.shortcuts import get_objects_for_user, assign_perm
from guardian.models import GroupObjectPermission


class UserViewSet(CheckPermViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        request.data['password'] = make_password(request.data['password'])
        serializer.is_valid(raise_exception=True)
        user = request.user
        user_groups = Group.objects.filter(user=user)
        if user.has_perm('app.add_%s' % self.basename):
            self.perform_create(serializer)
            if not user.is_superuser:
                mdl = self.get_serializer_class().Meta.model
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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if request.data['password'] != instance.password:
            request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = request.user
        if user.has_perm('change_%s' % self.basename, instance):
            self.perform_update(serializer)
        else:
            return Response(data='没有编辑权限，请联系管理员添加权限！', status=status.HTTP_403_FORBIDDEN)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class GetUserViewSet(CheckPermViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label

        objects = self.filter_queryset(self.get_queryset())
        queryset = get_objects_for_user(request.user, '%s.view_%s' % (app,self.basename), objects)

        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(CheckPermViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GetGroupViewSet(CheckPermViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GetGroupSerializer
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        mdl = self.get_serializer_class().Meta.model
        app = mdl._meta.app_label
        objects = self.filter_queryset(self.get_queryset())
        queryset = get_objects_for_user(request.user, '%s.view_%s' %(app, self.basename), objects)

        page_size = request.GET.get('limit')
        if int(page_size) == 10000:
            PageNumberPagination.page_size = None
        else:
            PageNumberPagination.page_size = page_size
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserPassword(APIView):
    def put(self, request, format=None):
        username = request.data['username']
        user = User.objects.get(username=username)
        if not check_password(request.data['old_password'],encoded=user.password) :
            return Response("旧密码错误", status=status.HTTP_400_BAD_REQUEST)
        user.password = make_password(request.data['password'])
        user.save()
        return Response("修改成功")


class ContentTypeViewSet(viewsets.ModelViewSet):
    queryset = ContentType.objects.filter(app_label='app')
    serializer_class = ContentTypeSerializer


class GetGroupObjectPermsView(APIView):
    def post(self, request, format=None):
        model = request.data['model']
        content_type = ContentType.objects.get(model=model)
        objects = request.data['objects']
        groupname = request.data['groupname']
        group = Group.objects.get(name=groupname)
        for i,object in enumerate(objects):
            perms = []
            object_pk = object['id']
            object_perms = GroupObjectPermission.objects.filter(content_type_id=content_type.id,object_pk=object_pk,group_id=group.id)
            for perm in object_perms:
                perms.append(perm.permission_id)
            object['perms'] = perms
            objects[i] = object
        return Response(objects)


class SetGroupObjectPermsView(APIView):
    def post(self, request, format=None):
        model = request.data['model']
        content_type = ContentType.objects.get(model=model)
        objects = request.data['objects']
        groupname = request.data['groupname']
        group = Group.objects.get(name=groupname)
        content_type_id = content_type.id
        group_id = group.id
        for i,object in enumerate(objects):
            object_pk = int(object['id'])
            e_perms = GroupObjectPermission.objects.filter(content_type_id=content_type_id,object_pk=object_pk,group_id=group_id)
            e_perms.delete()
            perms = object['perms']
            for permission_id in perms:
                gop = GroupObjectPermission(content_type_id=content_type_id,object_pk=object_pk,group_id=group_id,permission_id=permission_id)
                gop.save()
        return Response(status=status.HTTP_201_CREATED)


class GetGroupPermsView(APIView):
    def get(self, request):
        groupname = request.GET.get('groupname')
        group = Group.objects.get(name=groupname)
        # 查询组的所有记录
        queryset = GroupObjectPermission.objects.filter(group=group)
        # 获取模型
        content_types = queryset.values('content_type').distinct()
        results = []
        for content_type in content_types:
            # 获取模型对象
            objects = queryset.filter(content_type_id =content_type['content_type'])
            content_objects = []
            for object in objects:
                content_objects.append(object.content_object)
            content_objects=list(set(content_objects))
            group_objects = []
            model = ContentType.objects.get(pk=content_type['content_type']).model
            for content_object in content_objects:
                if content_object:
                    perms = objects.filter(object_pk = content_object.id).values('permission_id')
                    perm_dict = []
                    for perm in perms:
                        perm_dict.append(perm['permission_id'])
                    if model == 'host':
                        group_objects.append({'object': content_object.ip, 'perms': perm_dict})
                    else:
                        group_objects.append({'object': content_object.name, 'perms': perm_dict})
            results.append({'model':model , 'group_objects': group_objects})
        return Response(results)


