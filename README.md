+ La carpeta WEB es la carpeta raíz del proyecto.

+ En la carpeta Static Files se guardan todos los archivos estaticos de la app como imagenes o videos.

+ tablakarting es la carpeta principal del proyecto, es de donde se manejan las configuraciones del resto de las apps (archivos settings.py y urls.py basicamente) del proyecto.

+ En el archivo settings.py de la carpeta tablakarting (app principal del proyecto) se deben colocar todas las aplicaciones que se creen para que puedan funcionar correctamente. 
Especificamente en la variable INSTALLED_APPS. En este archivo también se puede manejar toda la info necesaria para una base de datos privada, KEYS y cosas relacionadas al servidor y archivos estaticos.


-------CARPETA WEB KARTING (APP)------

+ WebKarting es una aplicación del proyecto la cual se configura en parte desde la carpeta tablakarting en el archivo settings.proyecto

+ En WebKarting tenemos la estetica de la web dentro de la carpeta templates en archivos HTML.

+ El archivo admin.py se utiliza para declarar las tablas que queres visualizar en la sección admin de django que es 
de donde se puede visualizar el back en este framwork. Se entra desde el local host poniendo /admin.

+ En el archivo models.py se declaran las tablas de la base de datos a través de clases instanciadas.

+ En el archivo urls.py de la carpeta WebKarting se declara una lista con las url que se pasan como una función con parametros.
El primer path, en el primer parámetro no tiene nada porque representa el home.
El segundo parámetro llama una función declarada en el archivo views.py en la cual recibe info de las tablas en models.py
Y el tercer parámetro es simplemente la forma en la que aparece después de la barra en el navegador.

+ En el archivo views.py de la carpeta Web Karting (App) se encuentran las funcionalidades a través de las cuales se traen la info y se renderiza el html con la función render.
