# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page,Category
# Register your models here.
admin.site.register(Page)
admin.site.register(Category)