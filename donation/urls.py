from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('create_payment_intent/', views.create_payment_intent, name='create_payment_intent'),
    path('success/', views.successMsg, name='success'),
    # path('my_webhook_view/', views.my_webhook_view, name='my_webhook_view'),
]
