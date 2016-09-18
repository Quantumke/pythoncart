from django.db import models
from django_mongoengine import Document, EmbeddedDocument, DynamicDocument
from django_mongoengine import fields
from datetime import datetime, timedelta


# Create your models here.
class Item(models.Model):
	item_name=models.CharField(max_length=100)
	item_description=models.TextField(blank=False)
	item_slug=models.SlugField(max_length=100)
	item_link=models.SlugField(max_length=100)
	item_price=models.IntegerField(max_length=100)

	class Meta:
		verbose_name='items'
	def __str__(self):
		return self.item_name


class state_cart(models.Model):
	cart_item_name=models.CharField(max_length=100, unique=False)
	cart_item_description=models.CharField(max_length=500)
	cart_item_price=models.IntegerField(blank=True)
	cart_session_id=models.CharField(max_length=100)
	cart_slug=models.SlugField(max_length=100)
	quantity=models.IntegerField(blank=False)
	total_price=models.IntegerField(default=0,blank=True)
	date=models.DateTimeField(default=datetime.now)
	class Meta:
		verbose_name = "cart"
		verbose_name_plural = "carts"
	def __str__(self):
		return self.cart_item_name
