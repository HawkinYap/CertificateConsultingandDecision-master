from django.contrib import admin
from .models import UserProfile,UserInfo


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'stunamber', 'major')
    list_filter = ('major',)


admin.site.register(UserProfile, UserProfileAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "school", "major", "getcert", "address", "aboutme","img")
    list_filter = ("school", "major", "getcert")


admin.site.register(UserInfo, UserInfoAdmin)