# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.contrib import admin
# from rangoapp.models.category import Category
# from rangoapp.models.page import Page
# from rangoapp.models.user_profile import UserProfile
#
# # Register your models here.
# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug':('name',)}
# class PageAdmin(admin.ModelAdmin):
#     list_display = ('category','title','views')
#     list_filter =  ('category',)
#     ordering =  ('category','title')
#
# admin.site.register(Page,PageAdmin)
# admin.site.register(Category,CategoryAdmin)
# admin.site.register(UserProfile)