import pytest
from django.test import TestCase
from django.urls import reverse, NoReverseMatch
from django.test import Client

class TestUrls(TestCase):
    # 存在しないURLパターンを参照した際にエラーとなること
    def test_page_not_existed(self):
        with pytest.raises(NoReverseMatch):
            client = Client()
            response = client.get(reverse('logger:notexisted'))

    # indexページのURLが解決される
    def test_index_page(self):
        client = Client()
        response = client.get(reverse('logger:index'))
        self.assertEquals(response.status_code, 200)
    