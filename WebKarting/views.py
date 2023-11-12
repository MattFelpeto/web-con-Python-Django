from django.shortcuts import render
from .models import Piloto_Matias
from .models import Piloto_Fernando
from .models import Piloto_Jordy
from .models import Piloto_Pato
from .models import Piloto_Cristian
from .models import Piloto_Martincho
from .models import Piloto_Pedro
from .models import Piloto_Agustin
from .models import Fechas_Carreras

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def tabla_pos(request):
    Puntos_Matias = Piloto_Matias.objects.all()
    Puntos_Fernando = Piloto_Fernando.objects.all()
    Puntos_Jordy = Piloto_Jordy.objects.all()
    Puntos_Pato = Piloto_Pato.objects.all()
    Puntos_Cristian = Piloto_Cristian.objects.all()
    Puntos_Martincho = Piloto_Martincho.objects.all()
    Puntos_Pedro = Piloto_Pedro.objects.all()
    Puntos_Agustin = Piloto_Agustin.objects.all()
             
    return render(request, 'TablaPosiciones.html', {
        "Puntos_Matias": Puntos_Matias,
        "Puntos_Fernando": Puntos_Fernando,
        "Puntos_Jordy": Puntos_Jordy,
        "Puntos_Pato": Puntos_Pato,
        "Puntos_Cristian": Puntos_Cristian,
        "Puntos_Martincho": Puntos_Martincho,
        "Puntos_Pedro": Puntos_Pedro,
        "Puntos_Agustin": Puntos_Agustin,
    })

def historial_carreras(request):
    return render(request, 'historial.html', {})

def fechas_carreras(request):
    Pista = Fechas_Carreras.objects.all()
    return render(request, 'fechas.html', {
        "Pista": Pista,
    })