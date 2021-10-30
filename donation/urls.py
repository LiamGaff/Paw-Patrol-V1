from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('checkout/', views.create_checkout_session, name='checkout'),
    path('success/<str:args>/', views.success_msg, name='success'),
    path('wh/', views.stripe_webhook, name='webhook'),
]
