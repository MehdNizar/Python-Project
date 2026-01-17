from django.urls import path
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
=======
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
<<<<<<< HEAD
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
=======
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
]
