# -*- coding: utf-8 -*-

from django import forms
from rangoapp.models.page import Page

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Título da página.")
    url = forms.URLField(max_length=200,
        help_text="URL da página.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data

        url = cleaned_data.get('url')
        print(cleaned_data)
        print(url)

        url = url.lower()
        if url and not url.startswith('http://'):
            url = 'http://' + url
        cleaned_data['url'] = url

        return cleaned_data
    class Meta:
        model = Page
        exclude = ('category','likes','deslikes')