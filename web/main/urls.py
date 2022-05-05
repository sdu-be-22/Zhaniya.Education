from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('lib', views.lib, name='lib'),
    path('create', views.create, name='create'),
    path('login', views.login_request, name='login'),
    path('log_out', views.log_out, name='log_out'),
    path('register', views.register_request, name='register'),
]
