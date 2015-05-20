from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("You are at the home page")