from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('suma/', views.suma, name='suma'),
    path('ruido/', views.ruido, name='ruido'),
    path('random/', views.random_number, name='random_number'),
    path('<str:nombre>', views.saludo, name='saludo')
]
