# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    '''
    :param nome: models.CharField(max_length=128, unique=True)
    :param views = models.PositiveIntegerField(default=0)
    :param likes = models.PositiveIntegerField(default=0)
    :param deslikes = models.PositiveIntegerField(default=0)
    :param description = models.TextField(default=200)
    :param user = models.ForeignKey(User)
    :param is_private = models.BooleanField()
    :param slug = models.SlugField(unique=True)
    '''
    name = models.CharField(max_length=128, unique=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    deslikes = models.PositiveIntegerField(default=0)
    description = models.TextField(default=200)
    user = models.ForeignKey(User)
    is_private = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        '''Amplia o método save, modificando o atributo
        slug a cada salvamento, baseado no nome da categoria.'''
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse_lazy('category-detail', kwargs={'category_name_slug': self.slug})

    def __str__(self):
        return '%s' % self.name

    def __unicode__(self):
        return self.name
