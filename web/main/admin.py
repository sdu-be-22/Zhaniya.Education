from msilib.schema import Class
from django.contrib import admin
from .models import Classes, Task


admin.site.register(Task)
admin.site.register(Classes)