from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clientHome, name="clientHome"),
    path('createclient/', views.createclient, name="createclient"),
]