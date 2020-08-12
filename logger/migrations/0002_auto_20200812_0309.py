# Generated by Django 3.1 on 2020-08-12 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbosshistory',
            name='last_challenged_date',
        ),
        migrations.AddField(
            model_name='userbosshistory',
            name='challenged_date',
            field=models.DateField(default=datetime.date(2020, 8, 12), verbose_name='date challenged'),
        ),
    ]
