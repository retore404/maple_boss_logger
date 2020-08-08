from django.contrib import admin

from .models import Boss
from .models import UserBossHistory

admin.site.register(Boss)
admin.site.register(UserBossHistory)
