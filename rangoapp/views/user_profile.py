# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import *
from django.contrib.messages.views import SuccessMessageMixin
from rangoapp.models.user_profile import UserProfile
from rangoapp.forms.user import UserProfileForm
from rangoapp.models.page import Page
from django.utils.translation import ugettext_lazy as _

from rangoapp.permission.decorators import profile_required
from rangoapp.views.ranking import remove_points_friends, add_points_friends


class UserProfileListView(LoginRequiredMixin, ListView):
    # '''
    # Lista os perfis dos  usuário.
    # :URl: Sem URL
    # '''
    queryset = UserProfile.objects.all()
    paginate_by = 5

    def get_queryset(self):
        queryset = super(UserProfileListView, self).get_queryset()
        # queryset = queryset.filter(user=self.request.user)
        queryset = queryset.order_by("points", "id").reverse()
        return queryset


class UserProfileListByUserView(LoginRequiredMixin, ListView):
    '''
     Lista os perfis dos usuários.
    :URl: Sem URL
    '''
    queryset = UserProfile.objects.all()

    def get_queryset(self):
        queryset = super(UserProfileListByUserView, self).get_queryset()
        # queryset = queryset.filter(is_private=False,user__username=self.kwargs["username"])
        # queryset = queryset
        return queryset

#permissao na categoory
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    queryset = UserProfile.objects.all()
    #
    #
    # def get_context_data(self, **kwargs):
    #     context = super(UserProfileDetailView, self).get_context_data(**kwargs)
    #     return context


class UserProfileCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    '''
     Adiciona um perfil ao usuário.
    :URl: http://ip_servidor/userprofile/cadastrar/
    '''
    model = UserProfile
    form_class = UserProfileForm
    success_message = _("Profile of %(name)s add with successful! ")

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


class UserProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    '''
     Alterar o perfil do usuário.
    :URl: http://ip_servidor/userprofile/<pk>/update/
    '''
    model = UserProfile
    form_class = UserProfileForm
    success_message = _("User %(name)s changed with successful! ")

    # slug_field = 'username'
    # slug_url_kwarg = 'username'
    # form_class = UserProfileEditForm

    # def get_queryset(self):
    #     queryset = super(UserProfileUpdateView, self).get_queryset()
    #     queryset = queryset.filter(user__username=self.kwargs["username"])
    #     return queryset

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserProfileUpdateView, self).form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.user.username,
        )


class UserProfileDeleteView(LoginRequiredMixin, DeleteView):
    '''
     Deleta um perfil de usuário.
    :URl: Sem URL
    '''
    queryset = UserProfile.objects.all()
    success_url = reverse_lazy('user-profile-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super(UserProfileDeleteView, self).form_valid(form)


@login_required
def set_friend(request):
    '''
     Adiciona um amigo.
    :URl: http://ip_servidor/user/amigo/
    '''
    data = {}
    friend_username = request.GET.get('friend')
    # profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(UserProfile, user=request.user)
    # user = UserProfile.objects.filter(user=request.user)
    friend = get_object_or_404(User, username=friend_username)
    user_friend = UserProfile.objects.filter(user=user.user, friends__in=[friend])
    print(user_friend)
    # print(category)
    if friend:
        data["message"] = True
        if not user_friend:
            print("add")
            print(friend)
            print("in")
            print(user)
            user.friends.add(friend)
            remove_points_friends(friend)
            user.save()
            data['is_friend'] = True
            print("false")
        else:
            print("remove")
            print(friend)
            print("in")
            print(user)
            user.friends.remove(friend)
            user.save()
            data['is_friend'] = False
            add_points_friends(friend)
    else:
        data["message"] = False

    return JsonResponse(data)
