# Generated by Django 2.2.2 on 2019-09-13 16:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_auto_20190913_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 13, 16, 10, 14, 726131, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 13, 16, 10, 14, 726107, tzinfo=utc)),
        ),
    ]
