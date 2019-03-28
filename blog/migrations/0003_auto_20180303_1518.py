# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180303_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticles',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
