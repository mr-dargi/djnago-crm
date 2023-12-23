from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# change user model fields
UserAdmin.fieldsets[2][1]["fields"] = (
                                        "phone",
                                        "is_customer",
                                        "is_manager",
                                        "is_active",
                                        "is_staff",
                                        "is_superuser",
                                        "groups",
                                        "user_permissions",
                                      )

UserAdmin.list_display += ("is_manager", "is_customer", "phone")

admin.site.register(User, UserAdmin)