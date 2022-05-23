from msilib.schema import Class
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import *


admin.site.register(Theme)
admin.site.register(Classes)
admin.site.register(QuesModel)


class  MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass

admin.site.register(Video, MyModelAdmin)