from unicodedata import name
from urllib.parse import urlparse
from django.urls import path
from .import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),


    path('', views.profiles, name="profiles"),
    path('profile/<int:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('adminManage', views.adminManageAccount, name="adminManage"),
    path('delete-profile/<int:pk>/', views.adminDeleteAccount, name="delete-profile"), 
]