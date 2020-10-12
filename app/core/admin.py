from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from core import models


class UserAdmin(BaseUserAdmin):  # all of this is standard django admin
    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser",)}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    # wide means it will make the input field fullscreen
    # fieldsets are fields to be used when editing users
    # add_fieldsets are fields used when creating users


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
