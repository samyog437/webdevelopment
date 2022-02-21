from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.pic, name="pic"),
    path('picture/<int:pk>/',views.picture, name="picture"),  

    path('create-picture/', views.createPicture, name="create-picture"),
    path('update-picture/<int:pk>/', views.updatePicture, name="update-picture"),
    path('delete-picture/<int:pk>/', views.deletePicture, name="delete-picture"), 
 
]