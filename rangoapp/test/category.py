
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

    # def test_form_error(self):
    #     # print(self.client.get(reverse('category-add')))
    #     category = self.client.get(reverse('category-add'))
    #     category = category.form.submit()
    #     # self.assertContains(category, "This field is required.")

    # def test_form_success(self):
    #     page = self.app.get(self.entry.get_absolute_url())
    #     page.form['name'] = "Phillip"
    #     page.form['email'] = "phillip@example.com"
    #     page.form['body'] = "Test comment body."
    #     page = page.form.submit()
    #     self.assertRedirects(page, self.entry.get_absolute_url())

    # def test_valida_data(self):
    #     form = CategoryForm({
    #         'name': "DC",
    #         'description': "blabla",
    #         'is_private': False,
    #
    #     })
    #     self.assertTrue(form.is_valid())
    #     comment = form.save()
    #     self.assertEqual(comment.name, "DC")
    #     self.assertEqual(comment.description, "blabla")
    #     self.assertEqual(comment.is_private, False)
    #     self.assertEqual(comment.user, self.user_admin)
    def test_error_view_category(self):
        # self.assertTrue(self.client.login(username='admin', password='teste'))
        self.client.login(username='admin', password='teste')
        response = self.client.post(reverse('category-add'),
                                    {})
        # print(response)
        self.assertContains(response, "This field is required.")

    def test_view_category(self):
        self.client.login(username='admin', password='teste')
        response = self.client.post(reverse('category-add'),
                                    {'name': 'teste',
                                     'description': 'teste',
                                     }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "This field is required.")
        # self.assertRedirects(response, reverse("auth_login"))
        self.assertRedirects(response, reverse("category-detail", kwargs={"category_name_slug": 'teste'}))
        # print(teste)
        #
        # category = self.client.get(reverse('category-add'))
        # self.assertEqual(len(category.forms), 1)

    # def test_blank_data(self):
    #     form = CommentForm({}, entry=self.entry)
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors, {
    #         'name': ['required'],
    #         'email': ['required'],
    #         'body': ['required'],
    #     })
    def testUser(self):
        self.assertEquals(self.category_public.user.username, 'admin')

    def testSlug(self):
         category=get_object_or_404(Category,name='DC-flash')
         self.assertEquals('dc-flash', category.slug )

    def testObjectCreate(self):
        self.assertEquals(Category.objects.count(), 1)

        # activate('pt-br')
        # response = self.client.get(reverse("home"))
        # self.assertEquals(response, "template/rangoapp/index.html")
