# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from rangoapp.models.category import Category
from rangoapp.models.page import Page


class TestePage(TestCase):
    def setUp(self):
        self.category,new = Category.objects.get_or_create(
            name='DC-flash', views='2', likes='3'
        )
        self.page = Page.objects.get_or_create(
            title='DC-flash', url='hhtp://www.warnerchannel.com/br/flash/?ref=homefeature', category=self.category,
            views='2'
        )

    def tearDown(self):
        pass

    # def testUmMaisUm(self):
    #     self.assertEquals(1 + 1, 2)

    def testObjectCreate(self):
        self.assertEquals(Page.objects.count(), 1)
