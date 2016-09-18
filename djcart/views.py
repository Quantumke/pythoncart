from django.shortcuts import render, render_to_response, get_object_or_404
from djcart.models import *
import random
from django.db.models import Sum
from djcart.forms import AddToCart
from django.template import *
# Create your views here.
def home(request):
	context=RequestContext(request)
	items=Item.objects.all()
	return render_to_response('index.html', {
		'items':items
		}, context_instance=context)
def addcart(request, slug):
	session_id='nguruben@gmail.com'
	slug=slug
	item=Item.objects.get(item_link=slug)
	items=Item.objects.filter(item_link=slug)
	state_item=state_cart.objects.filter(cart_slug=item.item_link)
	count_items=state_item.count()
	print(count_items)
	quantity=count_items+1
	#print(quantity)
	cart_item_name=item.item_name
	cart_item_description=item.item_description
	cart_item_price=item.item_price
	cart_session_id=session_id
	cart_slug=item.item_slug
	quantity=quantity
	#total_price=state_item.aggregate(Sum('cart_item_price'))
	#total_price=total_price['cart_item_price__sum']
	last_id=state_cart.objects.filter(cart_session_id=session_id).latest('id')
	last_price=last_id.total_price
	print(last_price)
	if count_items ==0:
		total_price=cart_item_price
	else:
		total_price=last_price+cart_item_price
	#print(total_price)
	save=state_cart(cart_item_name=cart_item_name,
	cart_item_description=cart_item_description,
	 cart_item_price=cart_item_price,
	 cart_session_id=cart_session_id,
	 cart_slug=cart_slug,
	 quantity=quantity,
	 total_price=total_price)
	#save.save()

	return render_to_response('index.html',{
	 'cart_item_description':cart_item_description,
	 'cart_item_price':cart_item_price,
	  'quantity':quantity,
	 'total_price':total_price
		})

def view_cart(request):
	context=RequestContext(request)
	cart_items=state_cart.objects.all()
	print(cart_items)


	return render_to_response('cart.html', {
		'cart_items':cart_items
		}, context_instance=context)
def update_cart(request, id):
	context=RequestContext(request)
	#instance=state_cart.objects.get(id=id)
	if id:
		print(id)
	return render_to_response('update.html', {
		}, context_instance=context)
def cartadd(request):
	context=RequestContext(request)
	session_id='nguruben@gmail.com'
	if request.method=='POST':
		cart_item_name=request.POST['item_name']
		cart_item_description=request.POST['item_description']
		cart_item_price=request.POST['item_price']
		cart_session_id=session_id
		cart_slug=session_id
		quantity=request.POST['quantity']


		state_item=state_cart.objects.filter(cart_session_id=session_id)
		count_items=state_item.count()
		if count_items ==0:
			total_price=int(cart_item_price) * int(quantity)
		else:
			last_id=state_cart.objects.filter(cart_session_id=session_id).latest('id')
			last_price=last_id.total_price
			print(last_price)
			add_price=int(cart_item_price)*int(quantity)
			total_price=last_price+add_price
		print(cart_item_name,cart_item_description,
			cart_item_price,cart_session_id,cart_slug,quantity,total_price)
		save=state_cart(cart_item_name=cart_item_name,
	cart_item_description=cart_item_description,
	 cart_item_price=cart_item_price,
	 cart_session_id=cart_session_id,
	 cart_slug=cart_slug,
	 quantity=quantity,
	 total_price=total_price)
		save.save()
	return render_to_response('index.html', context_instance=context)



