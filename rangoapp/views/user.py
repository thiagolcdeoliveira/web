# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from django.views.generic import *
from rangoapp.forms.user import UserProfileForm, UserForm
from rangoapp.models.user_profile import UserProfile


class UserDetailView(DetailView):
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['profile'] = get_object_or_404(UserProfile,user__username=self.kwargs['username'])
        print(context['profile'])
        return context





class UserCreateView(View):
    template="rangoapp/register.html"
    context ={}
    def post(self,request,pk=None):
        self.context['user_form'] = UserForm(data=request.POST)
        self.context['profile_form'] = UserProfileForm(data=request.POST)
        if self.context['user_form'].is_valid() and self.context['profile_form'].is_valid():
            user = self.context['user_form'].save()
            user.set_password(user.password)
            user.save()
            profile = self.context['profile_form'].save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            messages.success(self.request, "Cadastrado com sucesso!", extra_tags='msg')
            self.context['user_form'] = UserForm()
            self.context['profile_form'] = UserProfileForm()
            return render(request,self.template,self.context)
        return render(request, self.template, self.context)

    def get(self,request,pk=None):
        self.context['user_form'] = UserForm()
        self.context['profile_form'] = UserProfileForm()
        return render(request,self.template,self.context)
