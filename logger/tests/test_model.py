import pytest
from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from django.test import Client
from django.contrib.auth.models import User
from logger.models import UserBossHistory, Boss
import datetime

class TestModels(TestCase):
    # マスタ読み込みをしていないとき，Bossテーブルが0件であること
    def test_is_boss_empty(self):
        boss_records = Boss.objects.all()
        self.assertEqual(boss_records.count(), 0)

    # 登録をしていないとき，UserBossHistoryテーブルが0件であること
    def test_is_empty_user_boss_history(self):
        user_boss_history_records = UserBossHistory.objects.all()
        self.assertEqual(user_boss_history_records.count(), 0)
    
    # Bossを1件追加したとき，登録されているレコードが1件であること
    def test_has_boss_one_record(self):
        boss = Boss()
        boss.save()
        boss_records = Boss.objects.all()
        self.assertEqual(boss_records.count(), 1)

    # UserBossHistoryを1件追加したとき，登録されているレコードが1件であること
    def test_has_user_boss_history_one_record(self):
        user_boss_history = UserBossHistory()
        user = User()
        user.save()
        boss = Boss()
        boss.save()
        dt = datetime.datetime.now()
        user_boss_history.user = user
        user_boss_history.boss = boss
        user_boss_history.last_challenged_date = dt        
        user_boss_history.save()
        user_boss_history_records = UserBossHistory.objects.all()
        self.assertEqual(user_boss_history_records.count(), 1)

    # 同じボス・ユーザに対して2件目のUserBossHistoryを追加したとき，
    # UpdateInsertではなくInsertされレコードが2件になること
    # UserBossHistoryを1件追加したとき，登録されているレコードが1件であること
    def test_has_user_boss_history_two_record(self):
        # レコードに登録するユーザとボスは同一
        user = User()
        user.save()
        boss = Boss()
        boss.name = 'BOSS'
        boss.save()
        
        # 1件目の登録
        user_boss_history1 = UserBossHistory()
        dt1 = datetime.datetime.now()
        user_boss_history1.user = user
        user_boss_history1.boss = boss
        user_boss_history1.last_challenged_date = dt1      
        user_boss_history1.save()

        # 2件目の登録
        user_boss_history2 = UserBossHistory()
        dt2 = datetime.datetime.now()
        user_boss_history2.user = user
        user_boss_history2.boss = boss
        user_boss_history2.last_challenged_date = dt2       
        user_boss_history2.save()

        # テーブルにレコードが2件ある
        user_boss_history_records = UserBossHistory.objects.all()
        self.assertEqual(user_boss_history_records.count(), 2)


