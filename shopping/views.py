from django.http.response import HttpResponse
from django.shortcuts import render_to_response

def index(request):
	return HttpResponse('Hello World')

def hello(request):
	return render_to_response('index.html', locals())
