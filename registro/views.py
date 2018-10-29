from django.shortcuts import render
from django.http import HttpResponse
from .models import Postulante
from .models import Perro
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

#importar user
#from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'postulantes':Postulante.objects.all(),'usuario':usuario,'perros':Perro.objects.all()})

def crear(request):
    run = request.POST.get('run','')
    nombre = request.POST.get('nombre','')
    fecha = request.POST.get('fechaNacimiento','')
    correo = request.POST.get('correo','')
    telefono = request.POST.get('telefono','')
    region = request.POST.get('region','')
    comuna = request.POST.get('comuna','')
    vivienda = request.POST.get('tipoVivienda','')
    contrasenia = request.POST.get('contrasenia','')

    postulante = Postulante(run=run, nombre=nombre, fecha=fecha, correo=correo, telefono=telefono, region=region, comuna=comuna, vivienda=vivienda, contrasenia= contrasenia)
    postulante.save()
    
    return render(request,'index')

def eliminar(request,id):
    postulante = Postulante.objects.get(pk = id)
    postulante.delete()
    return redirect('index')

def eliminar_perro(request,id):
    perro = Perro.objects.get(pk = id)
    perro.delete()
    return redirect('index')

def crear_perro(request):
    foto = request.FILES.get('fotos',False)
    nombre = request.POST.get('nombre','')
    raza = request.POST.get('raza','')
    descripcion = request.POST.get('descripcion','')
    estado = request.POST.get('estado','')

    perro = Perro(foto=foto,nombre=nombre,raza=raza,descripcion=descripcion,estado=estado)
    perro.save()
    return redirect('index')

def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    run = request.POST.get('run','')
    contrasenia = request.POST.get('contrasenia','')
    #user = authenticate(request,username=usuario, password=contrasenia)
    user = Postulante.objects.filter(run=run).filter(contrasenia=contrasenia)

    if user is not None:
        #auth_login(request, user)
        request.session['usuario'] = user[0].nombre
        request.session['id'] = user[0].id
        return redirect("index")
    else:
        return redirect("login")

@login_required(login_url='login')
def cerrar_session(request):
    del request.session['usuario']
    logout(request)
    return redirect('index')