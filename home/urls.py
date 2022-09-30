from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

urlpatterns = [
        path('', views.home, name='home'),
        path('catalog/', views.catalog, name='catalog'),
        path('register/', register, name='register'),
        path('login/', login, name='login'),
]
