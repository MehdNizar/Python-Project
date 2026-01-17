<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
from django.contrib.auth.decorators import login_required
from .models import Startup
from .forms import StartupForm

def home(request):
<<<<<<< HEAD
    startups = Startup.objects.all().order_by('-date_ajout')
=======
    startups = Startup.objects.all()
>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
    return render(request, 'startups/home.html', {'startups': startups})

def startup_detail(request, pk):
    startup = get_object_or_404(Startup, pk=pk)
    return render(request, 'startups/startup_detail.html', {'startup': startup})

@login_required
def add_startup(request):
    if request.method == 'POST':
        form = StartupForm(request.POST, request.FILES)
        if form.is_valid():
            startup = form.save(commit=False)
            startup.gerant = request.user
            startup.save()
            return redirect('home')
    else:
        form = StartupForm()
    return render(request, 'startups/add_startup.html', {'form': form})
<<<<<<< HEAD
=======

>>>>>>> e1914e1 (Sauvegarde locale avant synchronisation)
