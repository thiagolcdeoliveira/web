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


class AboutViews(View):
    context = {}
    template = 'rangoapp/about.html'

    def get(self, request):
        return render(request, self.template, self.context)
