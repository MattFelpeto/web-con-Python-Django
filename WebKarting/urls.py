from  django.urls import path
from . import views

#el primer argumento de path es el nombre que figura como rutra.
#Por lo contrario el argumento "name" es lo que se utiliza para indicar la ruta deseada en elementos como botones etc.

urlpatterns = [
    path('', views.home, name='home'),
    path('tabla_posiciones', views.tabla_pos, name="tabla-posiciones"),
    path('Historial', views.historial_carreras, name="historial-carreras"),
    path('fechas', views.fechas_carreras, name="fechas-carreras"),
    path('https://3dimensionate.com.ar', views.home)    
    ]