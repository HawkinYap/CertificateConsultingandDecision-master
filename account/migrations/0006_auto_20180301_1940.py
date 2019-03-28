# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180301_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='photo',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
    ]
