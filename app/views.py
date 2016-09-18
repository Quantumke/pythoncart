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
