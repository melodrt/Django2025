from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola, Mundo!")

def despedida(request):
    return HttpResponse("¡Adiós, Mundo!")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres un adulto.")
    else:
        return HttpResponse("No eres un adulto.")