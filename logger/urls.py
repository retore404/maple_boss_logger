from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'logger'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('detail/', views.detail, name='detail'),
    path('login/', auth_views.LoginView.as_view(template_name="logger/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="logger:index"), name='logout'),
]