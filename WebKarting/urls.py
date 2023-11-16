from  django.urls import path
from . import views

#el primer argumento de path es el nombre que figura como rutra.
#Por lo contrario el argumento "name" es lo que se utiliza para indicar la ruta deseada en elementos como botones etc.

urlpatterns = [
    path('', views.home, name='home'),
    path('tabla_posiciones', views.tabla_pos, name="tabla-posiciones"),
    path('Historial', views.historial_carreras, name="historial-carreras"),
    path('fechas', views.fechas_carreras, name="fechas-carreras"),
    path('https://3dimensionate.com.ar', views.home),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"), 
    path('register_user', views.register_user, name="register_user"),
    path('info_puntos', views.puntuacion, name='como_se_puntua')    
    ]