# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rangoapp.models.category import Category
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile

# Register your models here.

admin.site.register(UserProfile)