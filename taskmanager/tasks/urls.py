# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Autenticación
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Vistas de tareas
    path('', views.task_list, name='task_list'),  # Página principal
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
