# -*- coding: utf-8 -*-

from django import forms
from rangoapp.models import Category, Page

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Nome da categoria.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Título da página.")
    url = forms.URLField(max_length=200,
        help_text="URL da página.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)
