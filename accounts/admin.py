from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CreateUserAdminForm, ChangeUserAdminForm

User = get_user_model()


# Register your models here.
class CustomUserAdmin(UserAdmin):
    form = ChangeUserAdminForm
    add_form = CreateUserAdminForm
    # model = CustomUser
    list_display = ['email', 'admin', 'role']
    list_filter = ['admin', 'role', 'is_active']
    fieldsets = (
        (None, {
            'fields': ('email', 'password',)
        }),
        ('Personal info', {
            'fields': (
                ('first_name', 'last_name'), 'birth_date', 'phone_number',)
        }),
        ('Job info', {
            'fields': (('date_start_job', 'date_end_job'), ('region', 'role'),)
        }),
        ('Permissions', {
            'classes': ('collapse',),
            'fields': ('admin', 'is_superuser',)
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_confirm')
        }),
    )

    search_fields = ['email']
    ordering = ['email']


admin.site.register(User, CustomUserAdmin)
