from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile


# Create your models here.

class Folder(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='folder_owner')
    users = models.ManyToManyField(Profile, related_name='folder_users')
    name = models.CharField(max_length=75, blank=True)
    folders = models.ManyToManyField('self', related_name='folders')
    path = models.CharField(max_length=500, blank=True)
    #Genesis ID ROOT FOLDER ID
    g_id = models.IntegerField(blank=True)


def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])

class File(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='file_owner')
    users = models.ManyToManyField(Profile, related_name='file_users')
    path = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=75, blank=True)
    file_type = models.CharField(max_length=75, blank=True)
    files = models.FileField(upload_to=content_file_name, blank=True)
    images = models.ImageField(blank=True, upload_to='album')


