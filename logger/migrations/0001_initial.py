# Generated by Django 3.1 on 2020-08-10 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boss_name', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBossHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_challenged_date', models.DateTimeField(verbose_name='date challenged')),
                ('boss', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='logger.boss', to_field='boss_name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
