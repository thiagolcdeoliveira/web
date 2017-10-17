# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from rangoapp.models.user_profile import UserProfile
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm, RegistrationFormNoFreeEmail


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description','website', 'picture')




class UserProfileRegistrationForm(RegistrationFormNoFreeEmail):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
