# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','views')
    list_filter =  ('category',)
    ordering =  ('category','title')

admin.site.register(Page,PageAdmin)
admin.site.register(Category,CategoryAdmin)