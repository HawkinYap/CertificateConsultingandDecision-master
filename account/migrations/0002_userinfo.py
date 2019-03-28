# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=100, blank=True)),
                ('major', models.CharField(max_length=100, blank=True)),
                ('getcert', models.CharField(max_length=100, blank=True)),
                ('address', models.CharField(max_length=100, blank=True)),
                ('aboutme', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to=b'', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
