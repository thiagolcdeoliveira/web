# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rangoapp.models.category import *
from rangoapp.models.page import *
import csv
#from django.
import hashlib

from rangoapp.models.user_profile import UserProfile


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = '''Deve conter um csv intitulado "csv/aginas.csv" na raiz do projeto.'
           Deve conter os cabeçalhos:
           "category",
           "title",
           "url",
           "views"
           ".'''

    def _create_user(self):
        with open('csv/user_profile.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not User.objects.filter(username=row['username']):
                    user = User(
                        username=row["username"],
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        password=make_password(row["password"]),
                    )
                    user=user.save()
                # if not UserProfile.objects.filter(user=user):
                    userprofile = UserProfile(
                        user=User.objects.get(username=row["username"]),
                        description=row["description"],
                        picture=row["picture"],
                        points=0,


                    )
                    userprofile.save()

    def _create_category(self):
        with open('csv/category_page_new.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not Category.objects.filter(name=row['name']):
                    category = Category(
                        # category=Category.objects.get(name=row["category"]),
                                        name=row["name"],
                                        # url=row["url"],
                                        # views=row['views']
                                        is_private = False,
                                        user=User.objects.get(username=row['user'])
                                        

                                        )
                    category.save()

    def _create_page(self):
        with open('csv/paginas_category_new.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if not Page.objects.filter(title=row['title']):
                    pages = Page(category=Category.objects.get(name=row["category"]),
                                        title=row["title"],
                                        url=row["url"],
                                        views=row['views']

                                        )
                    pages.save()




    def handle(self, *args, **options):
        self._create_user()
        self._create_category()
        self._create_page()
