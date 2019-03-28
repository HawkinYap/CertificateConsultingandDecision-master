# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='user',
        ),
        migrations.DeleteModel(
            name='IMG',
        ),
    ]
