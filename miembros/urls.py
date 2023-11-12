from  django.urls import path
from . import views

#el primer argumento de path es el nombre que figura como rutra.
#Por lo contrario el argumento "name" es lo que se utiliza para indicar la ruta deseada en elementos como botones etc.

urlpatterns = [
      path('login_user', views.login_user, name="login"),
      path('logout_user', views.logout_user, name="logout"), 
      path('register_user', views.register_user, name="register_user")
    ]