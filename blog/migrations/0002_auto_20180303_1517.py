# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 3, 7, 17, 7, 909000, tzinfo=utc)),
        ),
    ]
