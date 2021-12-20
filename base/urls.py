from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('register/', views.RegisterPage, name='register'),
    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),
    path('profile/<str:pk>/', views.UserProfile, name='profile'),
    path('create-room/', views.CreateRoom, name="create-room"),
    path('update-room/<str:pk>/', views.UpdateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.DeleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.DeleteMessage, name="delete-message"),
    path('edit-user/', views.EditUser, name="edit-user"),
]