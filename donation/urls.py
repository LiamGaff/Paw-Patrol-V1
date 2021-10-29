from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.donate, name='donate'),
    path('create_payment_intent/', views.create_payment_intent, name='create_payment_intent'),
    path('success/', views.success_msg, name='success'),
    path('wh/', webhook, name='webhook'),
]
