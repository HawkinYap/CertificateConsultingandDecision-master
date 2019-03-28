# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0004_auto_20180227_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='users_like',
            field=models.ManyToManyField(related_name='articles_like', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 27, 12, 51, 10, 816000, tzinfo=utc)),
        ),
    ]
