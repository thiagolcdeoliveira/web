# -*- coding: utf-8 -*-
from django.test import TestCase

from django.core.urlresolvers import reverse
from django.utils.translation import activate


    # self.assertTemplateUsed(response, "taskbuster/index.html")


class TestLanguage(TestCase):
    def setUp(self):
        pass

    def test_language(self):
        self.language('en', '/en/accounts/login/')
        self.language('pt-br', '/pt-br/accounts/login/')
        self.language('es', '/es/accounts/login/')

    def language(self, language, login):
        activate(language)
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, login)
