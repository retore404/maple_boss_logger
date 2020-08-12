from django.db import models
from django.contrib.auth.models import User
import datetime

# ボス情報を管理するモデル
class Boss(models.Model):
    boss_name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.boss_name

# 各ユーザーのボス挑戦履歴を管理するモデル
class UserBossHistory(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.PROTECT)
    boss = models.ForeignKey(Boss, to_field='boss_name', on_delete=models.PROTECT)
    challenged_date = models.DateField('date challenged', default=datetime.date.today())