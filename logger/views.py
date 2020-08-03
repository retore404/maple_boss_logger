from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .forms import *

def index(request):
    return HttpResponse('Index dummy')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logger:index')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'logger/signup.html', context)
