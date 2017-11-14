# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db import models

from rangoapp.models.category import Category
from rangoapp.models.page import Page
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):

    '''
    :param user: models.OneToOneField(User)
    :param website: models.URLField(blank=True,help_text=_('website'))
    :param picture: models.ImageField(upload_to='profile_images', blank=True,help_text=_('picture'))
    :param points: models.FloatField(default=0)
    :param description: models.CharField(max_length=200,help_text=_('description'))
    :param friends: models.ManyToManyField(User, related_name='friends', blank=True)
    :param category_like: models.ManyToManyField(Category, related_name='category_like', blank=True)
    :param category_deslike: models.ManyToManyField(Category, related_name='category_deslike', blank=True)
    :param page_like: models.ManyToManyField(Page, related_name='page_like', blank=True)
    :param page_deslike: models.ManyToManyField(Page, related_name='page_deslike', blank=True)
    '''
    user = models.OneToOneField(User)
    website = models.URLField(blank=True,help_text=_('website'))
    picture = models.ImageField(upload_to='profile_images', blank=True,help_text=_('picture'))
    points = models.FloatField(default=0)
    description = models.CharField(max_length=200,help_text=_('description'))
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    category_like = models.ManyToManyField(Category, related_name='category_like', blank=True)
    category_deslike = models.ManyToManyField(Category, related_name='category_deslike', blank=True)
    page_like = models.ManyToManyField(Page, related_name='page_like', blank=True)
    page_deslike = models.ManyToManyField(Page, related_name='page_deslike', blank=True)

    def __str__(self):
        ''' 
        Define nome de exibição para o objeto
        '''
        return self.user.username

    def get_absolute_url(self):
        '''
        
        :return: Define a url de retorno após executar os metodos de create e Update
        '''
        # return reverse_lazy('user-detail', kwargs={'username': self.user.username})
        return reverse_lazy('user-change-detail', kwargs={'username': self.user.username})
