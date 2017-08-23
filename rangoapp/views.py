# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World! <a href = '/rango/about/'>about</a>")
#
# def about(request):
#     return HttpResponse("Hello World! <a href= '/rango/home/'>home</a> ")

def index(request):
    context_dict = {}
    bold_message = 'E aí, BSI, tudo em cima?'
    autor = 'Thiago'
    context_dict['bold_message'] = bold_message
    context_dict['autor'] = autor

    return render(request, 'rango/index.html', context_dict)

def about(request):

    return render(request, 'rango/about.html', {'autor':'Thiago'})