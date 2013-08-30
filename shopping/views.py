from django.shortcuts import render_to_response
from shopping.models import Product

def index(request):
	products = Product.objects.all()
	return render_to_response('index.html', locals())
