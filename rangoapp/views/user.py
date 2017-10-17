# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from django.views.generic import *
from rangoapp.forms.user import UserProfileForm, UserForm
from rangoapp.models.category import Category
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.views.ranking import calculatePosition
from registration.backends.default.views import RegistrationView
from rangoapp.forms.user import UserProfileRegistrationForm


class UserDetailView(DetailView):
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['profile'] = get_object_or_404(UserProfile,user__username=self.kwargs['username'])
        context['categories'] = Category.objects.filter(is_private=False,user__username=self.kwargs['username']).order_by('-likes')[:5]
        context['pages'] = Page.objects.filter(category__is_private=False,category__user__username=self.kwargs["username"]).order_by('-views')[:5]
        context['position'] = calculatePosition(context['profile'].points)
        print(context['profile'])
        return context

class MyRegistrationView(RegistrationView):

    form_class = UserProfileRegistrationForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)

        user_profile = UserProfile()
        user_profile.user = new_user
        user_profile.website = form_class.cleaned_data['wibsite']
        user_profile.save()
        return user_profile




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
