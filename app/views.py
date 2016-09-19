from django.shortcuts import render, render_to_response, get_object_or_404
from app.models import *
import random
from django.db.models import Sum
# Create your views here.

def home(request):
	items=Item.objects.all()
	return render_to_response('index.html', {
		'items':items
		})

#@login_required
def addcart(request, slug):
	session_id="nguruben@gmail.com"
	print(slug)
	slug=slug
	item=Item.objects.get(item_link=slug)
	items=cart.objects.filter(cart_session_id=session_id)
	a=items.aggregate(Sum('cart_item_price'))
	quantity=items.count()
	item_quantity=quantity+1
	cart_items={}
	cart_items['cart_item_name']=item.item_name
	cart_items['cart_item_description']=item.item_description
	cart_items['cart_item_price']=str(item.item_price)
	cart_items['cart_session_id']=session_id
	cart_items['cart_slug']=session_id
	cart_items['quantity']=str(item_quantity)
	#print (cart_items)
	save=cart(**cart_items)
	#save=state_cart(cart_item_name=item.item_name,cart_item_description=item.item_description, cart_item_price=item.item_price,cart_session_id=session_id)
	#save.save()
	return render_to_response('index.html',{
		'slug':slug
		})
