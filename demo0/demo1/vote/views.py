from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def vindex(request):
    vote = Vote.objects.all()
    return render(request, 'vote/index.html', {'vote': vote})


def vdetail(request, id):
    vote = Vote.objects.get(pk=id)
    if request.method == 'GET':

        # op = vote.option_set.all()
        return render(request, 'vote/detail.html', {'vote':vote})
    elif request.method == 'POST':
        optionid = request.POST.get('optionid')
        option = Option.objects.get(pk=optionid)
        option.num+=1
        option.save()
        return redirect(reverse('vote:result', args=(vote.id,)))

# 投票结果
def result(request, id):
    vote = Vote.objects.get(pk=id)
    return render(request, 'vote/result.html', {'vote':vote})
