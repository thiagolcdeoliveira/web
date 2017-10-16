# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import *

from rangoapp.models.category import Category
from rangoapp.models.page import  Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.views.ranking import calculatePosition


class IndexViews(View):
    context = {}
    template='rangoapp/index.html'


    def get(self,request):
        self.context['categories'] = Category.objects.filter(is_private=False).order_by('-likes')[:5]
        self.context['pages'] = Page.objects.filter(category__is_private=False).order_by('-views')[:5]
        self.context['profile'] = get_object_or_404(UserProfile,user=request.user)
        self.context['position'] = calculatePosition(self.context['profile'].points)
        return render(request, self.template, self.context)

