from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('lib', views.lib, name='lib'),
    # path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    re_path(r'^register/$', views.register, name='register'),
    path('log_out', views.log_out, name='log_out'),
    path('create', views.create, name='create'),
]
