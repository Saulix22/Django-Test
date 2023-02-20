from django.urls import path
from . import views 
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('materiales', views.materiales, name='materiales'),
    path('materiales/crear', views.crear, name='crear'),
    path('materiales/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('materiales/editar/<int:id>', views.editar, name='editar'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
