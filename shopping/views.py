from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from shopping.models import Product, Comment
from django.template.context import RequestContext

def index(request):
	products = Product.objects.all()
	return render_to_response('index.html', locals())

def show(request, resource_id):
	product = Product.objects.get(id=resource_id)
	comments = product.comment_set.all()
	return render_to_response('show.html', locals(), RequestContext(request))

def comment(request):
	product = Product.objects.get(id=request.POST['product'])
	Comment.objects.create(product=product, content=request.POST['comment'])
	return HttpResponseRedirect('/product/%s' % product.id)

def delete_comment(request, resource_id):
	comment = Comment.objects.get(id=resource_id)
	product_id = comment.product.id
	comment.delete()
	return HttpResponseRedirect('/product/%s' % product_id)
