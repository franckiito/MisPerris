from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include

#Api rest 
from registro.apirest import views_api
from rest_framework import routers

#Routers
router = routers.DefaultRouter()
router.register(r'postulantes', views_api.PostulanteViewSet)
router.register(r'perros', views_api.PerroViewSet)

urlpatterns = [
    path('',views.index, name = "index"),
    path('postulante/crear', views.crear, name = "crear"),
    path('postulante/eliminar/<int:id>', views.eliminar, name = "eliminar"),
    path('perro/crear', views.crear_perro, name = "crear_perro"),
    path('perro/eliminar/<int:id>', views.eliminar_perro, name = "eliminar_perro"),
    path('perro/editar/<int:id>', views.editar_perro, name = "editar_perro"),
    path('perro/editado/<int:id>', views.editado_perro, name = "editado_perro"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('login/recuperar',views.recuperar,name="recuperar"),
    path('login/recuperado',views.recuperado,name="recuperado"),
    
    path('lista/', include(router.urls)),
    path('accounts/profile/', views.cargar, name= "cargar"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
