from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog_post/', views.blog_post, name='blog_post'),
    path('<int:post_id>', views.view_post, name='view_post'),
]
