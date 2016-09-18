from django import forms
from djcart.models import *

class AddToCart(forms.ModelForm):
    class Meta:
        model = state_cart
        fields = ('cart_item_name','cart_item_description','cart_item_price','quantity')

class UpdateCart(forms.ModelForm):
	class Meta:
		model= state_cart
		fields=('quantity',)
