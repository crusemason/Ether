"""ether URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from core import views as core_views
from uploads import views as upload_views

from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', core_views.login, name='login'),
    path('users/', include('core.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('', upload_views.home, name='home'),

    path('uploads/', include('uploads.urls')),
    path('rootfolder/', upload_views.rootfolder),
    path('uploadfileat/', upload_views.uploadfileat),
    path('trash/', upload_views.mydrivetrash),
    path('starred/', upload_views.allStarred),
    path('makesubfolder/', upload_views.makesubfolder),
    path('subfolder/<int:pk>/', upload_views.subfolder, name='subfolder'),
    url(r'^trash/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', upload_views.trash, name='trash'),
    url(r'^trashfolder/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', upload_views.trashfolder, name='trashfolder'),
    url(r'^download/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', upload_views.download, name='download'),
    url(r'^downloadfolder/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', upload_views.downloadfolder, name='downloadfolder'),
    url(r'^star/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', upload_views.star, name='star'),
    url(r'^starfolder/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', upload_views.starfolder, name='starfolder'),
    url(r'^removestar/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', upload_views.removestar, name='removestar'),
    url(r'^ajax/validate_username/$', upload_views.validate_upload,                name='validate_upload'),
    url(r'^ajax/searchajax/$', upload_views.searchajax,                name='searchajax'),
    path('my_view_that_updates_pieFact/', upload_views.my_view_that_updates_pieFact),


]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
