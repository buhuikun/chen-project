from django.shortcuts import render,redirect, reverse
from .models import *
# Create your views here.

def index(reqest):
    questions = Question.objects.all()
    return render(reqest, 'polls/index.html', {'questions': questions})

def detail(request, id):
    question = Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'polls/detail.html', {'question': question})
    elif request.method == 'POST':
        optionid = request.POST.get('optionid')
        option = Options.objects.get(pk=optionid)
        option.vote += 1
        option.save()
        return redirect(reverse('polls:result', args=(question.id, )))

def result(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', {'question': question})


def addpoll(request):
    if request.method == 'GET':
        return render(request, 'polls/addpoll.html', {})

    elif request.method == 'POST':
        # 问题
        question = Question()
        question.title = request.POST.get('question')
        question.save()
        # 选项
        option1 = Options()
        option1.choice = request.POST.get('option1')
        option1.question = question
        option1.save()
        option2 = Options()
        option2.choice = request.POST.get('option2')
        option2.question = question
        option2.save()
        return redirect(reverse('polls:index'))


def delpoll(request, id):
    question = Question.objects.get(pk=id)
    question.delete()
    return redirect(reverse('polls:index'))

