# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import View
from rangoapp.forms.user import UserProfileForm, UserForm


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
            # self.context['registered'] = True
        # else:
        #     print(user_form.errors, profile_form.errors)
        return render(request, self.template, self.context)

    def get(self,request,pk=None):
        self.context['user_form'] = UserForm()
        self.context['profile_form'] = UserProfileForm()
        return render(request,self.template,self.context)
