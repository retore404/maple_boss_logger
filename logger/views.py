from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .forms import *
from .models import UserBossHistory, Boss
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'logger/index.html')

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

def register(request):
    if request.method == 'POST':
        form = BossRegisterForm(request.POST)
        if form.is_valid():
            # 入力値
            user = request.user # 操作中のユーザ情報
            boss_name = form.cleaned_data.get('boss_name')
            challenged_date = form.cleaned_data.get('challenged_date')
            
            # 入力値から対象のBossレコードを特定
            boss = Boss.objects.filter(boss_name=boss_name)[0]

            # データを追加
            user_boss_history = UserBossHistory(user=user, boss=boss, challenged_date=challenged_date)
            user_boss_history.save()
            return redirect('logger:index')
    else:
        form = BossRegisterForm()

    context = {'form':form}    
    return render(request, 'logger/register.html', context)

def detail(request):
    if request.user.is_authenticated:
        # 閲覧中のユーザ
        user = request.user
        
        # UserBossHistoryから閲覧中のユーザの記録を取得
        history = UserBossHistory.objects.filter(user=user)
        
        # contextに格納し画面へ
        context = {
            'history': history
        }
        return render(request, 'logger/detail.html', context)
    else:
        return redirect('logger:login')