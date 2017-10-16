# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rangoapp.models.category import Category
from rangoapp.models.page import  Page
from rangoapp.models.user_profile import UserProfile




def calculatePosition(points):
    user=UserProfile.objects.order_by('-points')
    position = [x for x,u in enumerate(user)  if u.points == points ]
    print(user[0].points)
    return  position[0]+1

