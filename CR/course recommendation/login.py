#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
import pymysql
import os
from django.shortcuts import render
from django.views.decorators import csrf

def index(request):
	return render_to_response('login.html')

    #HttpResponse("Hello world ! ")
def test(request):
	return render_to_response('webSet.html')

def login_post(request):
    request.encoding='utf-8'
    ctx ={}
    if 'username' in request.GET:
        ctx['username'] = request.GET['username']
    if 'password' in request.GET:
        ctx['password'] = request.GET['password']
    if not ctx['username']  or not ctx['password'] :
        return HttpResponse("Refused to log in! ")
    else:
        return render_to_response('index.html',ctx)