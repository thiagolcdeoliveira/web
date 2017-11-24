# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import *

from rangoapp.models.category import Category
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile
# from rangoapp.permission.decorators import my_login_required, profile_required
from rangoapp.permission.decorators import profile_required
from rangoapp.views.ranking import calculate_position
from datetime import datetime
from rangoapp.views.visitor import visitor_cookie_handler
from django.utils.translation import ugettext_lazy as _


@method_decorator(profile_required, name='dispatch')
class IndexViews(LoginRequiredMixin, View):
    context = {}
    template = 'rangoapp/index.html'

    def get(self, request):

        self.context['categories'] = Category.objects.filter(is_private=False).order_by('-likes')[:3]
        self.context['profile_request'] = UserProfile.objects.filter(user=request.user)
        self.context['profile_card'] = get_object_or_404(UserProfile, user=request.user)

        self.context['categories_friends'] = Category.objects.filter(is_private=False, user__in=self.context[
            'profile_card'].friends.all()).order_by('-likes')[:3]
        self.context['pages'] = Page.objects.filter(category__is_private=False).order_by('-views')[:3]

        if self.context['profile_request']:
            self.context['profile_request'] = self.context['profile_request'][0]
            self.context['position'] = calculate_position(self.context['profile_request'].points)
            # self.context['lightning'] = lightning(self.context['position'])
            # self.context['lightning'] = range(abs(int(self.context['position'].poitns / 10)))

        else:
            return HttpResponseRedirect(reverse('user-profile-add'))
        return render(request, self.template, self.context)
        #
        # def lightning(points):
        #     lightning={}
        #     lightning['yellow'] = range(abs(int(points / 10)))
        #     if len(lightning['yellow']) > 4:
        #         lightning['yellow'] = range(4)
        #     else:
        #         lightning['noyellow']= range(5-len(lightning['yellow']))
        #     return lightning
