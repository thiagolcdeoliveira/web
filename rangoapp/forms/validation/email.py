# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

def ValidationEmail(user,email):
    if not User.objects.filter(email=email) or User.objects.filter(email=email,username=user):
        return email
    else:
        # raise forms.ValidationError("Email já cadastrado!")
        raise forms.ValidationError(_("Email already existed!"))