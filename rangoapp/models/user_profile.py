# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    points  = models.FloatField(default=0)
    description  = models.CharField(max_length=200)
    # friends = models.ManyToManyField(User)
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
        return reverse_lazy('user-detail', kwargs={'username': self.user.username})