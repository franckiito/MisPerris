from django.shortcuts import render
from django.http import HttpResponse
from .models import Postulante

# Create your views here.

def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'nombre':"Franco",'elementos':["uno", "dos", "tres"],'postulantes':Postulante.objects.all()})

def registro(request):
    return render(request, 'formulario.html',{})

def crear(request):
    run = request.POST.get('run','')
    nombre = request.POST.get('nombre','')
    fecha = request.POST.get('fechaNacimiento','')
    correo = request.POST.get('correo','')
    telefono = request.POST.get('telefono','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')
    vivienda = request.POST.get('tipoVivienda','')

    postulante = Postulante(run=run, nombre=nombre, fecha=fecha, correo=correo, telefono=telefono, region=region, comuna=comuna, vivienda=vivienda)
    postulante.save()
    
    return render(request,'index.html')
