from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # Import UserAdmin
from .models import CustomUser
from rest_framework.authtoken.admin import TokenAdmin

class CustomUserAdmin(UserAdmin):
    # The fields to display in the list view of the admin panel
    list_display = UserAdmin.list_display + ('phone_number', 'bio', 'profile_picture')

    # The fields to show in the detailed user view when you click on a user
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('phone_number', 'bio', 'profile_picture')}),
    )

    # The fields to show in the "add user" page in the admin panel
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'bio', 'profile_picture')}),
    )

# Re-register the CustomUser model with our new custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

# Register the Token model in the admin for easy management
from rest_framework.authtoken.models import Token
admin.site.register(Token, TokenAdmin)