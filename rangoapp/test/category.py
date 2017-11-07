
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.translation import activate

from rangoapp.models.category import Category


class TesteCategory(TestCase):
    def setUp(self):
        # self.user, new = User.objects.get_or_create(
        #     username='admin'
        # )

        # self.category = Category.objects.get_or_create(
        #     name='DC-flash', views='2', likes='3',is_private=False
        # )
        pass

    # def tearDown(self):
    #     pass

    # def testUmMaisUm(self):
    #     self.assertEquals(1 + 1, 2)
    def testSlug(self):

         category=get_object_or_404(Category,name='DC-flash')
         self.assertEquals('dc-flash', category.slug )

    def testObjectCreate(self):
        # self.assertEquals(Category.objects.count(), 1)

        activate('pt-br')
        response = self.client.get(reverse("home"))
        self.assertEquals(response, "template/rangoapp/index.html")