from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Profile, Mobile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'region']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Mobile)