from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from shopping.models import Product, Comment, Favorite, User
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
	Comment.objects.create(user=request.user, product=product, content=request.POST['comment'])
	return HttpResponseRedirect('/product/%s' % product.id)

def delete_comment(request, resource_id):
	comment = Comment.objects.get(id=resource_id)
	product_id = comment.product.id
	comment.delete()
	return HttpResponseRedirect('/product/%s' % product_id)

@login_required
def favorite(request, resource_id):
	product = Product.objects.get(id=resource_id)
	Favorite.objects.get_or_create(user=request.user, product=product)
	return HttpResponseRedirect('/favorites')

@login_required
def favorites(request):
	favorites = Favorite.objects.filter(user=request.user)
	return render_to_response('favorites.html', locals())

def login(request):
	return render_to_response('login.html', locals(), RequestContext(request))

def authenticate(request):
	user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
	if user == None:
		return HttpResponse('username or password error')
	
	auth.login(request, user)
	return HttpResponseRedirect(request.POST.get('next', '/') or '/')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def signup(request):
	return render_to_response('signup.html', locals(), RequestContext(request))

def create(request):
	user = User.objects.create_user(username=request.POST['username'], 
									email=request.POST['email'],
									password=request.POST['password'])
	print 'create', user
	user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
	print 'authenticated', user
	auth.login(request, user)
	return HttpResponseRedirect(request.POST.get('next', '/') or '/')
