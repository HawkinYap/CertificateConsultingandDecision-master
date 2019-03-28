# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20180301_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='photo',
        ),
    ]
