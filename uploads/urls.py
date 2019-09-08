from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from django.conf.urls import url

from . import views

urlpatterns = [
        path('', views.home),
        path('upload/', views.upload),
        path('getDirs/', views.getDirs, name='getDirs'),
        path('handle_upload/', views.handle_upload, name='handle_upload'),
        ]

