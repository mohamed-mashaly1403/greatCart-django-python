from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import account,UserProfile
class account_admin(UserAdmin):
    def thumbnail(self,object):
        return format_html('<img width="50" style="border-radius:50%;"  src="{}" alt="user picture">'.format(object.image_url))
    list_display = ['thumbnail','email','first_name','last_name','joined_date','last_login','is_active']
    list_display_links = ['email','first_name']
    readonly_fields = ['joined_date','last_login']
    ordering = ('-joined_date','first_name')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
class userProfileAdmin(admin.ModelAdmin):

    list_display = ['user', 'city', 'state', 'country']

admin.site.register(account,account_admin)
admin.site.register(UserProfile,userProfileAdmin)

