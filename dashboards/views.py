from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse


def index(request):
	return render(request, 'dashboards/index.html')

def matches(request):
	return render(request, 'dashboards/matches.html')

def diagnosis(request):
	return render(request, 'dashboards/diagnosis.html')

def scheduler(request):
	return render(request, 'dashboards/scheduler.html')