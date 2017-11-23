# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, DetailView
from django.views.generic import *
from rangoapp.forms.user import UserProfileForm, UserForm
from rangoapp.models.category import Category
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.views.ranking import calculate_position
from registration.backends.default.views import RegistrationView
from rangoapp.forms.user import UserProfileRegistrationForm
from django.utils.translation import ugettext_lazy as _

class UserDetailView(DetailView):
    '''
     Detalhe do usuário.
    :URl: http://ip_servidor/user/visualizar/<username>
    '''
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        self.context = super(UserDetailView, self).get_context_data(**kwargs)
        self.context['profile_card'] = get_object_or_404(UserProfile,user__username=self.kwargs['username'])
        self.context['profile_request'] = get_object_or_404(UserProfile,user=self.request.user)
        self.context['categories'] = Category.objects.filter(is_private=False,user__username=self.kwargs['username']).order_by('-likes')[:3]
        self.context['pages'] = Page.objects.filter(category__is_private=False,category__user__username=self.kwargs["username"]).order_by('-views')[:3]
        self.context['position'] = calculate_position(self.context['profile_card'].points)
        print("%s -- -" %self.context['profile_card'])
        print(self.context['profile_request'])
        return self.context

class UserChangeDetailView(DetailView):
    '''
     Alterar um usuário.
    :URl: http://ip_servidor/user/visualizar/<username>/update
    '''
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name= 'auth/user_change_detail.html'

    def get_context_data(self, **kwargs):
        self.context = super(UserChangeDetailView, self).get_context_data(**kwargs)
        # self.context['profile_card'] = get_object_or_404(UserProfile,user__username=self.kwargs['username'])
        self.context['profile_request'] = get_object_or_404(UserProfile,user=self.request.user)
        return self.context

class MyRegistrationView(RegistrationView):
    # '''
    #  Adicionar um usuario.
    # :URl: http://ip_servidor/category/listar/
    # '''
    form_class = UserProfileRegistrationForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)

        user_profile = UserProfile()
        user_profile.user = new_user
        user_profile.website = form_class.cleaned_data['wibsite']
        user_profile.save()
        return user_profile




class UserUpdateView(SuccessMessageMixin,UpdateView):
    '''
     Alterar um usuário.
    :URl: http://ip_servidor/user/<username>/update
    '''
    model = User
    form_class = UserForm
    # form_class = PageEditForm
    slug_field = 'username'
    slug_url_kwarg = 'username'
    # template_name = 'registration/registration_form.html'
    success_message = _("user %(name)s change with succcessfull! ")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.username,
        )
    def get_success_url(self):
        return reverse_lazy('user-change-detail', kwargs={'username': self.object.username})

class UserDeleteView(SuccessMessageMixin,DeleteView):
    '''
     Deleta um usuario.
    :URl: http://ip_servidor/user/<pk>/delete
    '''
    queryset = User.objects.all()
    success_url = reverse_lazy('auth_logout')
    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # success_message = u"Usuário %(name)s deletado com sucesso! "
    success_message = _("user deactivated with successfull! ")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserDeleteView, self).form_valid(form)

    # def get_success_message(self, cleaned_data):
    #     return self.success_message % dict(
    #         cleaned_data,
    #         name=self.object.username,
    #     )
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        success_url = self.get_success_url()
        return HttpResponseRedirect(success_url)

class UserCreateView(View):
    '''
    Adicionar usuário.
   :URl: http://ip_servidor/user/cadastrar/
   '''
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
            messages.success(self.request, _("Add with successufull!"), extra_tags='msg')
            self.context['user_form'] = UserForm()
            self.context['profile_form'] = UserProfileForm()
            return render(request,self.template,self.context)
        return render(request, self.template, self.context)

    def get(self,request,pk=None):
        self.context['user_form'] = UserForm()
        self.context['profile_form'] = UserProfileForm()
        return render(request,self.template,self.context)
