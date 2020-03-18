from django.contrib import admin
from app.models import Env,Software,JavaPackage,Project
# Register your models here.
admin.site.register(Env)
admin.site.register(Software)
admin.site.register(JavaPackage)
admin.site.register(Project)
