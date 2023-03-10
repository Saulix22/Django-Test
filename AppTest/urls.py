from django.urls import path
from . import views 
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('iniciarSesion', views.iniciarSesion, name='iniciarSesion'),
    path('registro', views.registro, name='registro'),
    path('logout', views.cerrarSesion, name='logout'),
    path('materiales', views.materiales, name='materiales'),
    path('materiales/crear', views.crear, name='crear'),
    path('materiales/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('materiales/editar/<int:id>', views.editar, name='editar'),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('solicitudes/crear', views.crearSolicitud, name='crearSolicitud'),
    path('solicitudes/eliminar/<int:id>', views.eliminarSolicitud, name='eliminarSolicitud'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
