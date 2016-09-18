from django.contrib import admin
from djcart.models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	#prepopulated_fields=['item_name']
	pass
admin.site.register(Item, ItemAdmin)

class CartAdmin(admin.ModelAdmin):
	pass
admin.site.register(state_cart, CartAdmin)
