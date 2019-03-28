# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20180303_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='img',
            field=models.ImageField(upload_to=b'img', blank=True),
        ),
    ]
