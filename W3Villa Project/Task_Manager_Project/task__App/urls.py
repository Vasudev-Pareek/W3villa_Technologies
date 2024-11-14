from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignUp, name='SignUp'),  # Home page or Signup page
    path('Login/', views.Login, name='Login'),  # Login page
    path('viewusers/', views.viewusers, name="viewusers"),  # View all users
    path('saveEnquery/', views.saveEnquery, name="saveEnquery"),  # Save user on sign up
    path('Task-Manager/', views.TaskManager, name="TaskManager"),  # Task manager page
    path('LoginData/', views.LoginData, name='LoginData'),  # Login data handling
    path('add-to-do/', views.add_to_do, name='add_to_do'),
]