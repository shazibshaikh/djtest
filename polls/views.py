"""
Polls app view file
"""
from django.shortcuts import render, get_object_or_404
#from django.template import loader
from django.http import HttpResponse, Http404
from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    q =get_object_or_404(Question, pk=question_id,)
    return render(request, 'polls/detail.html', {'question':q})

def results(request, question_id):
    return HttpResponse("Results of Question %s." % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on Question %s." % question_id)