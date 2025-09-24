from django.http import HttpResponse

#request: Para realizar peticiones
#HttpResponse: Para enviar la respuesta usando el protocolo HTTP


#Esto es una vista simple que devuelve un mensaje de bienvenida
def bienvenida(request): #Pasamos un objeto de tipo request como primer parámetro
    return HttpResponse("¡Bienvenido a MiProyecto!")

def bienvenidaRojo(request):
    return HttpResponse("<h1 style='color:red;'>¡Bienvenido a MiProyecto pero esta vez de color rojo!</h1>")
