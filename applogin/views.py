# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import redirect


def home(request):

    if request.user.id:
        user=User.objects.filter(pk=request.user.id).last()
        if user.email:
            return redirect("evento-list")
        else:
            return redirect("user-email-add")
    else:
        return redirect("evento-list")