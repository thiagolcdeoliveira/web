# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
import datetime

from django.contrib.auth.models import User
from rangoapp.models.user_profile import UserProfile



class TesteUserProfile(TestCase):
    def setUp(self):
        # self.user, new = User.objects.get_or_create(
        #     username='admin'
        # )

        self.user, new = User.objects.get_or_create(
            username='admin'
        )
        self.user_profile = UserProfile.objects.get_or_create(
            website='http://www.com',  user=self.user
        )

    def tearDown(self):
        pass

    # def testUmMaisUm(self):
    #     self.assertEquals(1 + 1, 2)

    def testObjetosCriados(self):
        # self.assertEquals(User.objects.count(), 1)
        self.assertEquals(UserProfile.objects.count(), 1)
        # self.assertEquals(Category.objects.count(), 2)