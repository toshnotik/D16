from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'avatar')
