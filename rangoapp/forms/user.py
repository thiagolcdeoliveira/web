# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from rangoapp.forms.validation.email import ValidationEmail
from rangoapp.models.user_profile import UserProfile
from registration.forms import RegistrationFormUniqueEmail, RegistrationForm, RegistrationFormNoFreeEmail
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_checker = forms.CharField(required=True, label=_('Confirm Password'), widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password','password_checker')

    def clean_email(self):
        # print(self.cleaned_data.get("username"))
        return ValidationEmail(self.cleaned_data.get("username"),self.cleaned_data.get("email"))

    def clean_password_checker(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password_checker = self.cleaned_data['password_checker']
            if password == password_checker:
                return password_checker
            else:
                # raise forms.ValidationError('As senhas são diferentes!')
                raise forms.ValidationError(_('Passwords are different'))
        else:
            # raise forms.ValidationError('As senhas são diferentes!')
            raise forms.ValidationError(_('Password are differents!'))

    def save(self, commit=True):
        pessoa = super(UserForm, self).save(commit=False)
        pessoa.set_password(self.cleaned_data['password'])
        if commit:
            pessoa.save()
        return pessoa


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

    def clean_email(self):
        # print(self.cleaned_data.get("username"))
        return ValidationEmail(self.cleaned_data.get("username"), self.cleaned_data.get("email"))

    def save(self, commit=True):
        pessoa = super(UserForm, self).save(commit=False)
        pessoa.set_password(self.cleaned_data['password'])
        if commit:
            pessoa.save()
        return pessoa

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('description','website', 'picture')

    def clean_website(self):
        url = self.cleaned_data.get('website')
        url = url.lower()
        if url and not url.startswith('http://'):
            url = 'http://' + url
        self.cleaned_data['website'] = url
        return self.cleaned_data['website']


class UserProfileRegistrationForm(RegistrationFormNoFreeEmail):

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
