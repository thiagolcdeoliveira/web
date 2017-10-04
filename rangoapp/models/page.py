# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from rangoapp.models.category import Category


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Pages'
    def __str__(self):
        return '%s' %self.title

    def __unicode__(self):
         return self.title