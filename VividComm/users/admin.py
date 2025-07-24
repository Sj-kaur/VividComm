from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # Import UserAdmin
from .models import CustomUser

# Optional: Customize the admin display for CustomUser if needed
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['username', 'email', 'phone_number', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('phone_number', 'profile_picture', 'bio')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('phone_number', 'profile_picture', 'bio')}),
#     )

# Register your custom user model with the admin site
# Use the default UserAdmin or your custom one
admin.site.register(CustomUser)
# If you made CustomUserAdmin above, use: admin.site.register(CustomUser, CustomUserAdmin)