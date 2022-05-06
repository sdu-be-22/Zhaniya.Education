from msilib.schema import Class
from django.contrib import admin
from .models import Classes, QuesModel, Task


admin.site.register(Task)
admin.site.register(Classes)
admin.site.register(QuesModel)