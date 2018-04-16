from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from .models import Pages

# Create your views here.

def process(request, recurso):
    try:
        pagina = Pages.objects.get(name=recurso)
        respuesta = pagina.page
    except Pages.DoesNotExist:
        url_completa = "http://" + recurso
        with urllib.request.urlopen(url_completa) as w:
            respuesta = w.read()
            pagina = Pages(name = recurso, page = respuesta)
            pagina.save()
    return HttpResponse(respuesta)
