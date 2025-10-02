from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('suma/', views.suma, name='suma'),
    path('ruido/', views.ruido, name='ruido'),
    path('random/', views.random_number, name='random_number'),
    path('saludo/<str:nombre>', views.saludo, name='saludo'),
    path('about/', views.about, name='about'),
    path('tasks/', views.task_index, name='task_index'),
    path('tasks/add/', views.tasks_add, name='tasks_add'),
    path('tasks/admin/', views.tasks_admin_list, name='tasks_admin_list'),
    path("menu/",views.index2,name="index2")
]
