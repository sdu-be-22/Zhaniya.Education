from msilib.schema import Class
from django.contrib import admin
from .models import Classes, QuesModel, Theme


admin.site.register(Theme)
admin.site.register(Classes)
admin.site.register(QuesModel)