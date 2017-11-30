# -*- coding: utf-8 -*-

from django import forms
from rangoapp.models.page import Page
from django.utils.translation import ugettext_lazy as _
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text=_("Title of Page."))
    url = forms.URLField(max_length=200,
        help_text=_("URL of page."))
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean_url(self):
        url = self.cleaned_data.get('url')
        url = url.lower()
        if url and not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url
            self.cleaned_data['url'] = url

        return self.cleaned_data['url']
    class Meta:
        model = Page
        exclude = ('category','likes','deslikes')