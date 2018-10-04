from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

# Create your views here.

def index(request):
    return render(request,'index.html',{'nombre':"Franco",'elementos':["uno", "dos", "tres"]})

def registro(request):
    return render(request, 'formulario.html',{})

def crear(request):
    nombre = request.POST.get('nombre','')
    apellido = request.POST.get('apellido','')
    edad = request.POST.get('edad',0)
    persona = Persona(nombre=nombre, apellido=apellido, edad=edad)
    persona.save()
    
    return HttpResponse("nombre: "+nombre+" apellido: "+apellido)

