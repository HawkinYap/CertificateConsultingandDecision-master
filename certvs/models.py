from __future__ import unicode_literals

from django.db import models


class CertificateVs(models.Model):
    cert_id = models.AutoField(primary_key=True)
    cert_name = models.CharField(max_length=50)
    cert_dif = models.CharField(max_length=20)
    cert_quality = models.CharField(max_length=50)
    cert_condition = models.CharField(max_length=200)
    cert_time = models.CharField(max_length=200)
    cert_cost = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'certificate_vs'


