from django.urls import path
from . import views

urlpatterns = [
    path('', views.animals, name='animals'),
    path('add_animal/', views.add_animal, name='add_animal'),
    path('edit_animal/<int:animal_id>', views.edit_animal, name='edit_animal'),
]
