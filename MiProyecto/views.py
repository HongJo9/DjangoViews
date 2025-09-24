from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template

#request: Para realizar peticiones
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP


#Esto es una vista simple que devuelve un mensaje de bienvenida
def bienvenida(request): #Pasamos un objeto de tipo request como primer parámetro
    return HttpResponse("¡Bienvenido a MiProyecto!")

def bienvenidaRojo(request):
    return HttpResponse("<h1 style='color:red;'>¡Bienvenido a MiProyecto pero esta vez de color rojo!</h1>")

def categoriaEdad(request, edad):
    if edad < 18:
        if edad < 10:
            categoria = "niño"
        else:
            categoria = "adolescente"
    else:
        if edad < 65:
            categoria = "adulto"
        else:
            categoria = "adulto mayor"

    resultado = "<h1>Tu categoría de edad es: %s</h1>" %categoria
    return HttpResponse(resultado)

def obtenerMomentosActual(request):
    respuesta = "<h1>Fecha y hora actuales: {}</h1>".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
        <head>
            <title>Mi Proyecto Django</title>
        </head>
        <body>
            <h1 style="color:blue;">¡Bienvenido a Mi Proyecto Django!</h1>
            <p>Hola, mi nombre es %s y tengo %s años.</p>
            <p>Este es un ejemplo de contenido HTML servido desde una vista de Django.</p>
        </body>
    </html>
    """ %(nombre, edad)
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    # Abrir el archivo de la plantilla HTML
    plantillaExterna = open("MiProyecto/plantillas/miPrimeraPlantilla.html")
    # Cargar EL DOCUMENTO HTML como una plantilla de Django
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    # Crear un diccionario con el contexto
    contexto = Context()
    # Renderizar la plantilla con el contexto
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaParametros(request):
    nombre = "Luis"
    edad = 24
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lenguajes = ["Python", "JavaScript", "Java", "C#", "C++", "Ruby"]
    # Abrir el archivo de la plantilla HTML
    plantillaExterna = open("MiProyecto/plantillas/plantillaParametros.html")
    # Cargar EL DOCUMENTO HTML como una plantilla de Django
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    # Crear un diccionario con el contexto
    contexto = Context({"nombreCanal": nombre, "edad": edad, "fecha": fecha_actual, "lenguajes": lenguajes})
    # Renderizar la plantilla con el contexto
    documento = template.render(contexto)
    return HttpResponse(documento)

def plantillaCargador(request):
    nombre = "Luis"
    edad = 24
    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lenguajes = ["Python", "JavaScript", "Java", "C#", "C++", "Ruby", "go"]
    #Especificando la carpeta donde se encuentran las plantillas
    plantillaExterna = get_template("plantillaParametros.html")
    documento = plantillaExterna.render({"nombreCanal": nombre, "edad": edad, "fecha": fecha_actual, "lenguajes": lenguajes})
    return HttpResponse(documento)

