from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiares 
from django.template import loader

def muestra_base_datos(request):
    
    todos_los_familiares = Familiares.objects.all()
    print(todos_los_familiares)
    context = {'familiares': todos_los_familiares,}
    return render(request, 'plantilla.html', context = context)
