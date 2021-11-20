from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import account
class account_admin(UserAdmin):
    list_display = ['email','first_name','last_name','joined_date','last_login','is_active']
    list_display_links = ['email','first_name']
    readonly_fields = ['joined_date','last_login']
    ordering = ('-joined_date','first_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(account,account_admin)

