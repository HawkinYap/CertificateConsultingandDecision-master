from django.contrib import admin
from .models import CertificateVs


class CertificateVsAdmin(admin.ModelAdmin):
    list_display = ('cert_id', 'cert_name', 'cert_dif', 'cert_quality', 'cert_condition', 'cert_time', 'cert_cost')


admin.site.register(CertificateVs, CertificateVsAdmin)
