from django.urls import path
from . import views
from examen2.views import *

urlpatterns = [
    path("", views.Index, name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('todos/', views.todo_list, name='todo-list'),
    path('todos/id-title/', views.todo_id_title_list, name='todo-id-title-list'),
    path('todos/unresolved/', views.todo_unresolved_list, name='todo-unresolved-list'),
    path('todos/resolved/', views.todo_resolved_list, name='todo-resolved-list'),
    path('todos/user/', views.todo_user_list, name='todo-user-list'),
    path('todos/resolved/user/', views.todo_resolved_user_list, name='todo-resolved-user-list'),
    path('todos/unresolved/user/', views.todo_unresolved_user_list, name='todo-unresolved-user-list'),
]