from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .models import Miembros
from .forms import MiembrosForm
from django.contrib.auth.decorators import login_required, user_passes_test

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


@login_required
def welcome(request):
    return render(request, 'welcome.html')

def es_adulto(user):
    try:
        miembro = Miembros.objects.get(user=user)
        return miembro.edad >= 18
    except Miembros.DoesNotExist:
        return False

@user_passes_test(es_adulto)
def restricted_view(request):
    return render(request, 'restricted.html')

def es_color_celeste(user):
    try:
        miembro = Miembros.objects.get(user=user)
        return miembro.color_favorito.lower() == 'celeste'
    except Miembros.DoesNotExist:
        return False

@user_passes_test(es_color_celeste)
def color_celeste(request):
    return render(request, 'color_celeste.html')