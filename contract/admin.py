from django.contrib import admin
from .models import Contract


class ContractAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'body')
    list_filter = ('user',)


admin.site.register(Contract, ContractAdmin)
