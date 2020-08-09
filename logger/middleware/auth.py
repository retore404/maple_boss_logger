from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse


class authMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # 以下のすべて条件に当てはまるとき，ログインページにリダイレクトする
        # - ログインしていない
        # - loggerのログインページ以外のページにアクセスしようとしている
        # - adminサイト以外にアクセスしようとしている
        if not request.user.is_authenticated and request.path != '/logger/login/' and request.path[0:6] != '/admin':
            return HttpResponseRedirect(reverse('logger:login'))
        return response