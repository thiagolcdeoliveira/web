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

from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile


class TestPage(TestCase):
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
        self.page = Page(title='flash', category=self.category_public)
        self.page.save()

    def test_error_view_page(self):
        self.client.login(username='admin', password='teste')
        # self.user_admin.is_superuser=True
        # self.user_admin.save()
        # print(reverse('page-add', kwargs={'category_name_slug': 'dc-flash'}))
        response = self.client.post(reverse('page-add', kwargs={'category_name_slug': 'dc-flash'}),
                                    {})

        self.assertContains(response, "This field is required.")

    def test_view_page(self):
        self.client.login(username='admin', password='teste')
        response = self.client.post(reverse('page-add', kwargs={'category_name_slug': 'dc-flash'}),
                                    {'title': 'teste',
                                     'description': 'teste',
                                     'url': 'flash.com'
                                     }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "This field is required.")
        # self.assertRedirects(response, reverse("auth_login"))
        # print(response.request)
        # self.assertRedirects(response, reverse("category-detail", kwargs={'category_name_slug':'dc-flash'}))

        #
        # # def test_point_by_category(self):
        # #     profile = get_object_or_404(UserProfile, user=self.user_admin)
        # #     print(profile.points)
        #

    def testUser(self):
        self.assertEquals(self.page.category.user.username, 'admin')
        #
        # def testSlug(self):
        #      category=get_object_or_404(Category,name='DC-flash')
        #      self.assertEquals('dc-flash', category.slug )
        #

    def testObjectCreate(self):
        self.assertEquals(Page.objects.count(), 1)
