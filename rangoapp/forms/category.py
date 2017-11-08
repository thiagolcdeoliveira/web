# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User

from rangoapp.models.category import Category
from django.utils.translation import ugettext_lazy as _

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text=_("name of category."))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    is_private = forms.BooleanField(required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    # paginas = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'ui dropdown'}))

    class Meta:
        model = Category
        fields = ('name','is_private')

