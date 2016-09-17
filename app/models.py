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
class cart_session(DynamicDocument):
	session_id=fields.StringField(max_length=100, unique=True)
	session_date=fields.DateTimeField(blank=False, default=datetime.now)

