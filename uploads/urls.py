from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from django.conf.urls import url

from . import views

urlpatterns = [
        path('', views.home),
        path('upload/', views.upload),
        path('ajax/', views.getDirs),
        path('my_view_that_updates_pieFact/', views.my_view_that_updates_pieFact, name='my_view_that_updates_pieFact'),
        path('getDirs/', views.getDirs, name='getDirs'),
        path('handle_upload/', views.handle_upload, name='handle_upload'),
        path('mydrive/', views.mydrive, name='mydrive'),
        path('starred/', views.allStarred, name='allStarred'),
        path('recent/', views.recent, name='recent'),
        url(r'^ajax/validate_upload/$', views.validate_upload, name='validate_username'),

]

