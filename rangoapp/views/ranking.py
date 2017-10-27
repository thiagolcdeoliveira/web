# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rangoapp.models.category import Category
from rangoapp.models.page import Page
from rangoapp.models.user_profile import UserProfile
from rangoapp.models.category import Category


# from


def calculate_position(points):
    user = UserProfile.objects.order_by('-points')
    position = [x for x, u in enumerate(user) if u.points == points]
    print(user[0].points)
    return position[0] + 1


def add_points_category(user):
    profile = UserProfile.objects.get(user=user)
    profile.points += 0.2
    profile.save()

def remove_points_category(user):
    profile = UserProfile.objects.get(user=user)
    profile.points -= 0.2
    profile.save()


def add_points_page(user):
    profile = UserProfile.objects.get(user=user)
    profile.points += 0.5
    profile.save()

def remove_points_page(user):
    profile = UserProfile.objects.get(user=user)
    profile.points -= 0.5
    profile.save()


def add_points_like_category(user):
    profile = UserProfile.objects.get(user=user)
    profile.points += 0.5
    profile.save()


def remove_points_like_category(user):
    profile = UserProfile.objects.get(user=user)
    profile.points -= 0.5
    profile.save()


def add_points_friends(user):
    profile = UserProfile.objects.get(user=user)
    profile.points += 0.3
    profile.save()

def add_points_deslike_category(user):
    profile = UserProfile.objects.get(user=user)
    profile.points -= 0.5
    profile.save()


def remove_points_deslike_category(user):
    profile = UserProfile.objects.get(user=user)
    profile.points += 0.5
    profile.save()

def add_points_like_page(user):
    profile = UserProfile.objects.get(user=user)
    profile.points += 0.2
    profile.save()


def remove_points_like_page(user):
    profile = UserProfile.objects.get(user=user)
    profile.points -= 0.2
    profile.save()


def add_points_deslike_page(user):
    profile = UserProfile.objects.get(user=user)
    profile.points -= 0.2
    profile.save()


def remove_points_deslike_page(user):
    profile = UserProfile.objects.get(user=user)
    profile.points += 0.2
    profile.save()
