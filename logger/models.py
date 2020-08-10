from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import datetime
from django.utils import timezone

# ボス情報を管理するモデル
class Boss(models.Model):
    class LimitType(models.TextChoices):
        UNKNOWN = 'UN', 'Unknown'
        DAILY = 'DA', 'Daily'
        WEEKLY = 'WE', 'Weekly'

    boss_name = models.CharField(max_length=60, unique=True)
    boss_reward_meso = models.IntegerField(default=0)
    boss_limit_type = models.CharField(
        max_length=2,
        choices=LimitType.choices,
        default=LimitType.UNKNOWN,
    )

    def __str__(self):
        return self.boss_name

# 各ユーザーのボス挑戦履歴を管理するモデル
class UserBossHistory(models.Model):
    user = models.ForeignKey(User, to_field='username', on_delete=models.PROTECT)
    boss = models.ForeignKey(Boss, to_field='boss_name', on_delete=models.PROTECT)
    challenged_date = models.DateField('date challenged', default=timezone.now)

    def GetWeeklyTotalReward(user_id, start_date, end_date):
        # rawの結果にはidというフィールドが含まれる必要があるので無理やり作る
        query = """
            select
                0 as id,
                ifnull(sum (b.boss_reward_meso),0) as total_reward
            from
                logger_userbosshistory as bh 
                left join logger_boss as b 
                    on bh.boss_id = b.boss_name 
            where
                bh.user_id = '{}' 
                and bh.challenged_date between '{}' and '{}'
            """
        #TODO ここSelfとか使えないんか？
        result = UserBossHistory.objects.raw(query.format(user_id, start_date, end_date))
        return result[0].total_reward
    
    def GetWeeklyDefeatedBossCount(user_id, start_date, end_date):
        # rawの結果にはidというフィールドが含まれる必要があるので無理やり作る
        query = """
            select
                0 as id,
                count(*) as boss_count
            from
                logger_userbosshistory as bh 
                left join logger_boss as b 
                    on bh.boss_id = b.boss_name 
            where
                bh.user_id = '{}' 
                and bh.challenged_date between '{}' and '{}'
            """
        #TODO ここSelfとか使えないんか？
        result = UserBossHistory.objects.raw(query.format(user_id, start_date, end_date))
        return result[0].boss_count
    
    def GetWeeklyDefeatedBosses(user_id, start_date, end_date):
        query = """
            select
                b.id as id,
                date(bh.challenged_date) as date
            from
                logger_userbosshistory as bh 
                left join logger_boss as b 
                    on bh.boss_id = b.boss_name 
            where
                bh.user_id = '{}' 
                and bh.challenged_date between '{}' and '{}'
            order by
                date(bh.challenged_date) asc,
                b.id asc
        """
        result = UserBossHistory.objects.raw(query.format(user_id, start_date, end_date));
        r_dict = dict()
        for b in result:
            if b.date in r_dict:
                r_dict[b.date].append(b.id)
            else:
                r_dict[b.date] = [b.id]
        return r_dict