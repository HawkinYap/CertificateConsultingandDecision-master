# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=500)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(default=datetime.datetime(2018, 2, 27, 7, 44, 27, 9000, tzinfo=utc))),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(related_name='article', to=settings.AUTH_USER_MODEL)),
                ('column', models.ForeignKey(related_name='article_column', to='article.ArticleColumn')),
            ],
            options={
                'ordering': ('-updated',),
            },
        ),
        migrations.AlterIndexTogether(
            name='articlepost',
            index_together=set([('id', 'slug')]),
        ),
    ]
