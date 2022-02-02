from django.urls import path
from . import views

urlpatterns = [
    path('',views.pic, name="pic"),
    path('picture/<str:pk>/',views.picture, name="picture"),    
]