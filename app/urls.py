from django.contrib import admin
from django.urls import path, re_path

from .views import get_main_page

urlpatterns = [
    path('', get_main_page),
    re_path(r'^(?P<menu>[-\w/]+)/materials/(?P<path>[-\w/]+/)*(?P<title>[\w-]+)$', get_main_page),
]