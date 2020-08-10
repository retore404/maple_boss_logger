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

