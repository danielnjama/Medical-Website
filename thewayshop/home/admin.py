from django.contrib import admin

# Register your models here.
from . models import *


class shopAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':("name",)}
    list_display =("name","category","price","publish","datepost")
    list_editable=("publish","price")


admin.site.register(shop,shopAdmin)