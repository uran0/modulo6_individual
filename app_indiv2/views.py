from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .models import Miembros

def landing(request):
    return render(request, "landing.html")

def user_detail(request):
    miembros = Miembros.objects.all()
    context = {'miembros': miembros}
    return render(request, 'user_detail.html', context)