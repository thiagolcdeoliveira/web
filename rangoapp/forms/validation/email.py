# coding: utf-8
from django import forms
from django.contrib.auth.models import User


def ValidationEmail(user,email):
    if not User.objects.filter(email=email) or User.objects.filter(email=email,username=user):
        return email
    else:
        raise forms.ValidationError("Email já cadastrado!")