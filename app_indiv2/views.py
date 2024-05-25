from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .models import Miembros
from .forms import MiembrosForm

def landing(request):
    return render(request, "landing.html")

def user_detail(request):
    miembros = Miembros.objects.all()
    context = {'miembros': miembros}
    return render(request, 'user_detail.html', context)

def register(request):
    if request.method == 'POST':
        form = MiembrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_success')
    else:
        form = MiembrosForm()
    return render(request, 'register.html', {'form': form})

def register_success(request):
    return render (request,'register_success.html')