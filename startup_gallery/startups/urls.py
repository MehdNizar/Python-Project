from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('startup/<int:pk>/', views.startup_detail, name='startup_detail'),
    path('add/', views.add_startup, name='add_startup'),
]