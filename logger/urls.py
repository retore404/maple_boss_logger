from django.urls import path

from . import views

app_name = 'logger'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
]