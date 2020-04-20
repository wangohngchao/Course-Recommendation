from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import numpy as np

def hello(request):
	context          = {}
	context['hello'] = a()
	return render(request, 'hello.html', context)

    #HttpResponse("Hello world ! ")
def a():
	return 1
	pass