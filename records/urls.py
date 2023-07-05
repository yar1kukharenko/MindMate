from django.contrib import admin
from django.urls import path, include

from records.views import index

from django.conf.urls.static import static

from django.conf import settings

app_name = index

urlpatterns = [
    path('', index, name='index')
]
