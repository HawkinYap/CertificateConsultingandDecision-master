from django.contrib import admin
from .models import CertificateTbl
# Register your models here.
class CertificateTblAdmin(admin.ModelAdmin):
    list_display = ('cert_id', 'cert_class', 'cert_name', 'cert_time', 'cert_link')
    list_filter = ('cert_class', 'cert_name')
    search_fields = ('cert_name', 'cert_ename')
    raw_id_field = ('cert_name')
    ordering = ['cert_id','cert_name']

admin.site.register(CertificateTbl, CertificateTblAdmin)