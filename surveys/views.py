from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):
	question_list = Question.objects.all()
	context = {'question_list': question_list}
	return render(request, 'surveys/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def candidate(request):
	return render(request, 'surveys/candidate.html')

def company(request):
	return render(request, 'surveys/company.html')

def entrance(request):
	return render(request, 'surveys/entrance.html')

def exit(request):
	return render(request, 'surveys/exit.html')