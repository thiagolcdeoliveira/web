# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.ImageField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        '''Amplia o método save, modificando o atributo
        slug a cada salvamento, baseado no nome da categoria.'''
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return '%s' %self.name

    def __unicode__(self):
        return self.name