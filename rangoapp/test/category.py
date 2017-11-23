
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.translation import activate

from rangoapp.forms.category import CategoryForm
from rangoapp.models.category import Category

from django.test import Client

from rangoapp.models.user_profile import UserProfile


class TestCategory(TestCase):
    def setUp(self):
        activate('en')
        self.user_admin = User(
            username='admin', password=make_password('teste')
        )
        self.user_admin.save()
        self.user_admin_profile = UserProfile(
            user=self.user_admin
        )
        self.user_admin_profile.save()
        self.category_public = Category(
            name='DC-flash', views='2', likes='3', is_private=False, user=self.user_admin
        )
        self.category_public.save()
        pass


    def test_error_view_category(self):
        self.client.login(username='admin', password='teste')
        response = self.client.post(reverse('category-add'),
                                    {})
        self.assertContains(response, "This field is required.")

    def test_view_category(self):
        self.client.login(username='admin', password='teste')
        response = self.client.post(reverse('category-add'),
                                    {'name': 'teste',
                                     'description': 'teste',
                                     }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "This field is required.")
        self.assertRedirects(response, reverse("category-detail", kwargs={"category_name_slug": 'teste'}))

    def testUser(self):
        self.assertEquals(self.category_public.user.username, 'admin')

    def testSlug(self):
         category=get_object_or_404(Category,name='DC-flash')
         self.assertEquals('dc-flash', category.slug )

    def testObjectCreate(self):
        self.assertEquals(Category.objects.count(), 1)
