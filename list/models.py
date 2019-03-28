# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CertificateTbl(models.Model):
    cert_id = models.AutoField(primary_key=True)
    cert_class = models.IntegerField()
    cert_name = models.CharField(max_length=20)
    cert_ename = models.CharField(max_length=50)
    cert_content = models.CharField(max_length=1000)
    cert_time = models.CharField(max_length=1000)
    cert_qualif = models.CharField(max_length=1000)
    cert_relate = models.CharField(max_length=1000, blank=True, null=True)
    cert_intro = models.CharField(max_length=1000)
    cert_link = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'certificate_tbl'

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'
