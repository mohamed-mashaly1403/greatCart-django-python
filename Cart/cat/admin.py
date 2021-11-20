from django.contrib import admin
from .models import cat

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug':('cat_name',)}
    list_display = ( 'cat_name','cat_img')
admin.site.register(cat,catadmin)
# Register your models here.
