from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('user', 'title','url')
    list_filter = ('title',)


admin.site.register(Image, ImageAdmin)
