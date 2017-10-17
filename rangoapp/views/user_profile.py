# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from rangoapp.models.user_profile import UserProfile
from rangoapp.forms.user import UserProfileForm
from rangoapp.models.page import Page

class UserProfileListView(ListView):
    queryset = UserProfile.objects.all()

    def get_queryset(self):
        queryset = super(UserProfileListView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

class UserProfileListByUserView(ListView):
    queryset = UserProfile.objects.all()

    def get_queryset(self):
        queryset = super(UserProfileListByUserView, self).get_queryset()
        queryset = queryset.filter(is_private=False,user__username=self.kwargs["username"])
        return queryset

#permissao na categoory
class UserProfileDetailView(DetailView):
    queryset = UserProfile.objects.all()
    #
    #
    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileDetailView, self).get_context_data(**kwargs)
    #     return context

class UserProfileCreateView(SuccessMessageMixin,CreateView):
    model = UserProfile
    form_class = UserProfileForm
    success_message = "Perfil %(name)s cadastrado com sucesso! "

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        # messages.success(self.request, "Cadastrado com sucesso!", extra_tags='msg')
        return super(UserProfileCreateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.user.username,
        )

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    # form_class = UserProfileEditForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserProfileUpdateView, self).form_valid(form)


class UserProfileDeleteView(DeleteView):
    queryset = UserProfile.objects.all()
    success_url = reverse_lazy('user-profile-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserProfileDeleteView, self).form_valid(form)
