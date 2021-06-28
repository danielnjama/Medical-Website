from django.contrib import admin

# Register your models here.
from . models import *


class shopAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':("name",)}
    list_display =("name","category","datepost")
    list_editable=("category",)


admin.site.register(shop,shopAdmin)