from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import Piloto_Matias
from .models import Piloto_Fernando
from .models import Piloto_Jordy
from .models import Piloto_Pato
from .models import Piloto_Cristian
from .models import Piloto_Martincho
from .models import Piloto_Yoa
from .models import Fechas_Carreras
from .models import Piloto_Guada

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
    Puntos_Yoa = Piloto_Yoa.objects.all()
    Puntos_Guada = Piloto_Guada.objects.all()
    
             
    return render(request, 'TablaPosiciones.html', {
        "Puntos_Matias": Puntos_Matias,
        "Puntos_Fernando": Puntos_Fernando,
        "Puntos_Jordy": Puntos_Jordy,
        "Puntos_Pato": Puntos_Pato,
        "Puntos_Cristian": Puntos_Cristian,
        "Puntos_Martincho": Puntos_Martincho,
        "Puntos_Yoa": Puntos_Yoa,        
        "Puntos_Guada": Puntos_Guada,
    })

def historial_carreras(request):
    return render(request, 'historial.html', {})

def fechas_carreras(request):
    Pista = Fechas_Carreras.objects.all()
    return render(request, 'fechas.html', {
        "Pista": Pista,
    })
    
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        
        else:
            messages.success(request, ("Error al iniciar sesión, intente de nuevo."))
            return redirect('login')
            
    else:    
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("Saliste de la sesión"))
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registro exitoso."))
            return redirect('home')
    else:
        form = UserCreationForm() 
            
    return render(request, 'register_user.html', {
        'form': form,
    })    