# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.db import models

# Create your models here.
from rangoapp.models.category import Category
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128,help_text=_('title'))
    url = models.URLField(help_text=_('url'))
    description= models.TextField(default=200, help_text=_('description'))
    views = models.IntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    deslikes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Pages'

    def get_absolute_url(self):
        return reverse_lazy('category-detail', kwargs={'category_name_slug': self.category.slug})

    def __str__(self):
        return '%s' %self.title

    def __unicode__(self):
         return self.title