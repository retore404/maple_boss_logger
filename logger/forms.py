from django.contrib.auth.models import User
from django import forms
from . import models
import datetime
from .models import Boss
from django.contrib.admin.widgets import AdminDateWidget

class SignUpForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    enter_password = forms.CharField(widget=forms.PasswordInput)
    retype_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username has been already taken.')
        return username

    def clean_enter_password(self):
        password = self.cleaned_data.get('enter_password')
        if len(password) < 5:
            raise forms.ValidationError('Password must contain 5 or more characters.')
        return password

    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('enter_password')
        retyped = self.cleaned_data.get('retype_password')
        if password and retyped and (password != retyped):
            self.add_error('retype_password', 'This does not match with the above.')

    def save(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('enter_password')
        new_user = User.objects.create_user(username = username)
        new_user.set_password(password)
        new_user.save()

class BossRegisterForm(forms.Form):
    # 入力項目の定義
    boss_name = forms.ModelChoiceField(models.Boss.objects, label='ボス', to_field_name="boss_name")
    datetime = forms.DateField(
        label='日付',
        required=True,
        widget=AdminDateWidget()
    )

    # 精査
    # ボスIDの精査
    def clean_boss(self):
        boss_name = self.cleaned_data.get('boss_boss_name').boss_name
        if not Boss.objects.filter(boss_name=boss_name).exists():
            raise forms.ValidationError('ボスが存在しません')
        return boss_name
