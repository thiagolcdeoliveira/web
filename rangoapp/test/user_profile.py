# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import datetime

from django.contrib.auth.models import User
from django.urls import reverse

from rangoapp.models.user_profile import UserProfile



class TesteUserProfile(TestCase):
    def setUp(self):
        self.user, new = User.objects.get_or_create(
            username='admin'
        )
        self.user_profile = UserProfile.objects.get_or_create(
            website='http://www.com',  user=self.user
        )

    def test_view_category(self):
        response = self.client.post(reverse('registration_register'),
                                    {
                                        'username': 'teste',
                                        'email': 'email@gmail.com',
                                        'password1': 'root1234',
                                        'password2': 'root1234'
                                    }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("registration_complete"))


    def testObjetosCriados(self):
        self.assertEquals(UserProfile.objects.count(), 1)
