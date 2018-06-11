from django.shortcuts import render, HttpResponse  # HttpResponse: nos permite contestar a una peticion devolviendo un codigo

# Create your views here.
def home(request): #request: es la peticion (de que se quiere ver la portada en la pagina)
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about-me.html")

def contact(request):
    return render(request, "core/contact.html")       