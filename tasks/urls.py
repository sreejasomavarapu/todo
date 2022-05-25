from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.list,name="list"),
    path('update_task/<str:pk>/',views.Update_task,name="update_task"),
    path('delete/<str:pk>/',views.Delete,name="delete")
]