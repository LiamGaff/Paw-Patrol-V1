from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('messageForm/', views.messageForm, name='messageForm')
]
