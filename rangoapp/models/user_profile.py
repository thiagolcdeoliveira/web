# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db import models

from rangoapp.models.category import Category
from rangoapp.models.page import Page


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    points = models.FloatField(default=0)
    description = models.CharField(max_length=200)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    category_like = models.ManyToManyField(Category, related_name='category_like', blank=True)
    category_deslike = models.ManyToManyField(Category, related_name='category_deslike', blank=True)
    page_like = models.ManyToManyField(Page, related_name='page_like', blank=True)
    page_deslike = models.ManyToManyField(Page, related_name='page_deslike', blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy('user-detail', kwargs={'username': self.user.username})
