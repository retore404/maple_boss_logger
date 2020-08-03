from django.db import models
from django.contrib.auth.models import User

# ボス情報を管理するモデル
class Boss(models.Model):
    boss_id = models.CharField(max_length=3, unique=True)
    boss_name = models.CharField(max_length=60)

# 各ユーザーのボス挑戦履歴を管理するモデル
class UserBossHistory(models.Model):
    user_id = models.ForeignKey(User, to_field='username', on_delete=models.PROTECT)
    boss_id = models.ForeignKey(Boss, to_field='boss_id', on_delete=models.PROTECT)
    last_challenged_date = models.DateTimeField('date challenged')