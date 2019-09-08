# Generated by Django 2.2.2 on 2019-08-30 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=75)),
                ('path', models.CharField(blank=True, max_length=500)),
                ('g_id', models.IntegerField(blank=True)),
                ('folders', models.ManyToManyField(related_name='_folder_folders_+', to='uploads.Folder')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='folder_owner', to='accounts.Profile')),
                ('users', models.ManyToManyField(related_name='folder_users', to='accounts.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(blank=True, max_length=500)),
                ('name', models.CharField(blank=True, max_length=75)),
                ('file_type', models.CharField(blank=True, max_length=75)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='file_owner', to='accounts.Profile')),
                ('users', models.ManyToManyField(related_name='file_users', to='accounts.Profile')),
            ],
        ),
    ]