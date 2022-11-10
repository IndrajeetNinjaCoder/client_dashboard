from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projectHome, name="projectHome"),
    path('newproject/', views.newproject, name="newproject"),
]