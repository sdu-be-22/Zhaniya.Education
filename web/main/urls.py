from django.urls import path, re_path
from . import views
from .views import *
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('lib', views.lib, name='lib'),
    path('create', views.create, name='create'),
    path('login', views.login_request, name='login'),
    path('log_out', views.log_out, name='log_out'),
    path('register', views.register_request, name='register'),
    path('themes/<str:classes>/', views.themes, name='themes'),
    path('tasks/<str:classes>/', views.tasks, name='tasks'),
    path('videoles/<str:classes>/', views.videoles, name='videoles'),
    path('clas', views.clas, name='clas'),
    path('addtask', views.addtask, name='addtask'),
    path('addvideo', views.addvideo, name='addvideo'),
    path('addbook', views.addbook, name='addbook'),
]
