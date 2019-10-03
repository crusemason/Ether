from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from django.conf.urls import url

from . import views
app_name = 'uploads'
urlpatterns = [
        path('', views.mydrive),
        path('upload/', views.upload),
        url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^basic-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
    url(r'^progress-bar-upload/$', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    url(r'^drag-and-drop-upload/$', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
        path('ajax/', views.getDirs),
        path('my_view_that_updates_pieFact/', views.my_view_that_updates_pieFact, name='my_view_that_updates_pieFact'),
        path('getDirs/', views.getDirs, name='getDirs'),
        path('handle_upload/', views.handle_upload, name='handle_upload'),
        path('mydrive/', views.mydrive, name='mydrive'),
        path('mydrivetable/', views.mydrivetable, name='mydrivetable'),
        path('starred/', views.allStarred, name='allStarred'),
        path('recent/', views.recent, name='recent'),
        url(r'^ajax/validate_upload/$', views.validate_upload, name='validate_username'),



]

