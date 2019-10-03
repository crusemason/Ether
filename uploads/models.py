from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from django.utils import timezone

def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

# Create your models here.
class File(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='file_owner')
    users = models.ManyToManyField(Profile, related_name='file_users')
    path = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=75, blank=True)
    file_type = models.CharField(max_length=75, blank=True)
    files = models.FileField(upload_to=content_file_name, blank=True)
    size = models.CharField(max_length=1000,blank=True)
    file = models.FileField(upload_to='uploads/', default='',blank=True)
    images = models.ImageField(blank=True, upload_to='album')
    starred = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())




class Folder(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='folder_owner')
    folderfiles = models.ManyToManyField(File, related_name='folderfiles')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='folder_parent', blank=True, null=True)
    users = models.ManyToManyField(Profile, related_name='folder_users')
    name = models.CharField(max_length=75, blank=True)
    children = models.ManyToManyField('self', related_name='folders')
    path = models.CharField(max_length=500, blank=True)
    starred = models.BooleanField(default=False)
    #Genesis ID ROOT FOLDER ID
    trash = models.BooleanField(default=False)
    gid = models.IntegerField(default=0)

class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


