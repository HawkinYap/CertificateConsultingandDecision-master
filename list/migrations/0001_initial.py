# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateTbl',
            fields=[
                ('cert_id', models.AutoField(serialize=False, primary_key=True)),
                ('cert_class', models.IntegerField()),
                ('cert_name', models.CharField(max_length=20)),
                ('cert_ename', models.CharField(max_length=50)),
                ('cert_content', models.CharField(max_length=1000)),
                ('cert_time', models.CharField(max_length=1000)),
                ('cert_qualif', models.CharField(max_length=1000)),
                ('cert_relate', models.CharField(max_length=1000, null=True, blank=True)),
                ('cert_intro', models.CharField(max_length=1000)),
                ('cert_link', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
                'db_table': 'certificate_tbl',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': True,
            },
        ),
    ]
