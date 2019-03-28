# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('url', models.URLField()),
                ('slug', models.SlugField(max_length=500, blank=True)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('image', models.ImageField(upload_to=b'images/%Y/%m/%d')),
                ('user', models.ForeignKey(related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
