from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from .forms import *
from .models import UserBossHistory, Boss
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta
import json

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

def bossList(request):
    # 先週の木曜日を取得。 0:月曜日 ... 6:日曜日
    def getStartDate(date):
        day_diff = 3 - date.weekday()
        if day_diff > 0:
            day_diff -= 7
        return date + timedelta(days=(day_diff)) 

    if request.user.is_authenticated:
        #TODO ウィークリーとデイリーのボス上手い事分けたUI作る
        bosses = Boss.objects.all()
        current_date = date.today()
        start_date = getStartDate(current_date)
        end_date = start_date + timedelta(days=6) #TODO 終了日の境界値周りを治す
        #TODO この辺りもJson渡してJSでやりたい
        weekly_count = UserBossHistory.GetWeeklyDefeatedBossCount(request.user, start_date, end_date)
        weekly_total_reward = UserBossHistory.GetWeeklyTotalReward(request.user, start_date, end_date)
        day_defeated_bosses = UserBossHistory.GetWeeklyDefeatedBosses(request.user, start_date, end_date)

        params = {
                    'start_date': start_date.strftime("%Y-%m-%d"),
                    'end_date': end_date.strftime("%Y-%m-%d"),
                    'current_date': current_date.strftime("%Y-%m-%d"),
                    'bosses': bosses,
                    'weekly_count': weekly_count,
                    'weekly_total_reward': weekly_total_reward,
                    'day_defeated_bosses': json.dumps(day_defeated_bosses),
                }
        return render(request, 'logger/bossList.html', params)
    else:
        return redirect('logger:login')