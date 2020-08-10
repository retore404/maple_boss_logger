import pytest
from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from django.test import Client
from django.contrib.auth.models import User

class TestUrls(TestCase):
    # 存在しないURLパターンを参照した際にエラーとなること
    def test_page_not_existed(self):
        with pytest.raises(NoReverseMatch):
            client = Client()
            response = client.get(reverse('logger:notexisted'))

    # indexページのURLが解決される
    def test_index_page(self):
        client = Client()
        client.force_login(User.objects.create_user('test_user'))
        response = client.get(reverse('logger:index'))
        self.assertEquals(response.status_code, 200)
    
    # signupページのURLが解決される
    def test_signup_page(self):
        client = Client()
        response = client.get(reverse('logger:signup'))
        self.assertEquals(response.status_code, 200)

    # registerページのURLが解決される（ログイン時）
    def test_register_page_authenticated(self):
        client = Client()
        client.force_login(User.objects.create_user('test_user'))
        response = client.get(reverse('logger:register'))
        self.assertEquals(response.status_code, 200)

    # registerページのURLからリダイレクトされる（非ログイン時）
    def test_register_page_not_authenticated(self):
        client = Client()
        client.logout()
        response = client.get(reverse('logger:register'))
        self.assertRedirects(response, reverse('logger:login'), status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    # detailページのURLが解決される（ログイン時）
    def test_detail_page_authenticated(self):
        client = Client()
        client.force_login(User.objects.create_user('test_user'))
        response = client.get(reverse('logger:detail'))
        self.assertEquals(response.status_code, 200)

    # detailページのURLからリダイレクトされる（非ログイン時）
    def test_detail_page_not_authenticated(self):
        client = Client()
        client.logout()
        response = client.get(reverse('logger:detail'))
        self.assertRedirects(response, reverse('logger:login'), status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    # loginページのURLが解決される
    def test_login_page(self):
        client = Client()
        response = client.get(reverse('logger:login'))
        self.assertEquals(response.status_code, 200)

    # logoutページのURLからリダイレクトされる（非ログイン時）
    def test_logout_page_not_authenticated(self):
        client = Client()
        client.force_login(User.objects.create_user('test_user'))
        response = client.get(reverse('logger:logout'))
        self.assertRedirects(response, reverse('logger:login'), status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
    