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

@login_required
def register(request):
    if request.method == 'POST':
        form = BossRegisterForm(request.POST)
        if form.is_valid():
            # 入力値
            user = request.user # 操作中のユーザ情報
            boss_id = form.cleaned_data.get('boss_id')
            datetime = form.cleaned_data.get('datetime')
            
            # 入力値から対象のBossレコードを特定
            boss = Boss.objects.filter(boss_id=boss_id)[0]

            # データを更新（不存在であれば追加）
            obj, created = UserBossHistory.objects.update_or_create(
                user_id=user, boss_id=boss,
                defaults={'last_challenged_date': datetime}
            )
            return redirect('logger:index')
    else:
        form = BossRegisterForm()

    context = {'form':form}    
    return render(request, 'logger/register.html', context)

@login_required
def detail(request):
    # 閲覧中のユーザ
    user = request.user
    
    # UserBossHistoryから閲覧中のユーザの記録を取得
    history = UserBossHistory.objects.filter(user_id=user)

    # contextに格納し画面へ
    context = {
        'history': history
    }
    return render(request, 'logger/detail.html', context)