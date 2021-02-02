from django.contrib import admin
from app.models import *
from guardian.admin import GuardedModelAdmin
# Register your models here.
# class SoftwareProject(GuardedModelAdmin):
#     list_display = ('name',)


class L2MenuAdmin(GuardedModelAdmin):
    list_display = ('title', 'parent')

# admin.site.register(Host,HostAdmin)
admin.site.register(Env)
admin.site.register(Software)
admin.site.register(L1Menu)
# admin.site.register(L2Menu)

admin.site.register(L2Menu, L2MenuAdmin)
