from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = "index"),
    path('registro/crear', views.crear, name = "crear"),
    path('registro/crear_perro', views.crear_perro, name = "crear_perro"),
    path('registro/eliminar/<int:id>', views.eliminar, name = "eliminar"),
    path('registro/eliminar_perro/<int:id>', views.eliminar_perro, name = "eliminar_perro"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
