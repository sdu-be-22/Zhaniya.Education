from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    image = models.ImageField(upload_to='task_images', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Classes(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'классы'

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question