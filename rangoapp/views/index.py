# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import *

from rangoapp.models.category import Category
from rangoapp.models.page import  Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.views.ranking import calculate_position
from datetime import datetime
from rangoapp.views.visitor import visitor_cookie_handler
@method_decorator(login_required,name='dispatch')
class IndexViews(View):
    context = {}
    template='rangoapp/index.html'

    def get(self,request):
        self.context['categories'] = Category.objects.filter(is_private=False).order_by('-likes')[:3]
        self.context['pages'] = Page.objects.filter(category__is_private=False).order_by('-views')[:3]
        # self.context['profile'] = get_object_or_404(UserProfile,user=request.user)
        self.context['profile'] = UserProfile.objects.filter(user=request.user)
        if self.context['profile']:
            self.context['profile'] = self.context['profile'][0]
            self.context['position'] = calculate_position(self.context['profile'].points)
            self.context['lightning'] = lightning(self.context['position'])

        else:
            return HttpResponseRedirect(reverse('user-profile-add'))
        return render(request, self.template, self.context)

def lightning(points):
    lightning={}
    lightning['yellow'] = range(abs(int(points / 10)))
    if len(lightning['yellow']) > 4:
        lightning['yellow'] = range(4)
    else:
        lightning['noyellow']= range(5-len(lightning['yellow']))
    return lightning