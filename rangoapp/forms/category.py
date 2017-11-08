# -*- coding: utf-8 -*-
from django import forms
from rangoapp.models.category import Category
from django.utils.translation import ugettext_lazy as _


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           label=_('name'),
                           help_text=_('must contain a maximum of 128 characters'))
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 5}),
                                  label=_('description'),
                                  help_text=_('must contain a maximum of 200 characters'))
    is_private = forms.BooleanField(required=False,
                                    label=_('is private'))

    class Meta:
        model = Category
        fields = ('name', 'description', 'is_private')
