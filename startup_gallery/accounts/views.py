from django.shortcuts import render, redirect
<<<<<<< HEAD
from django.contrib.auth import login
=======
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
<<<<<<< HEAD
=======

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
