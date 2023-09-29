from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def inicio(request):
    return render(request,"AppLacasona/inicio.html")

def newsletter(request):

#    if request.method == 'POST':
#        nuevomailfornl = Newsletter(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
#        nuevomailfornl.save()
#        return render(request,"AppLacasona/inicio.html")    
    return render(request, "AppLacasona/see_newsletter.html")

def sendsong(request):
    return render(request,"AppLacasona/see_sendsong.html")

def askanything(request):
    return render(request,"AppLacasona/see_askanything.html")


def form_mailfornl(request):
    if request.method == 'POST':
        nuevomailfornl = Newsletter(nombre=request.POST["nombre"], apellido=request.POST["apellido"], email=request.POST["email"])
        nuevomailfornl.save()
        return render(request,"AppLacasona/inicio.html")
    
    return render(request, "AppLacasona/form_newsletter.html")

def form_sendsong(request):
    if request.method == 'POST':
        nuevoformsong = SendSong(songname=request.POST["songname"], email=request.POST["email"], url=request.POST["url"])
        nuevoformsong.save()
        return render(request,"AppLacasona/inicio.html")
    
    return render(request, "AppLacasona/form_sendsong.html")

def form_askanything(request):
    if request.method == 'POST':
        nuevoformask = AskAnything(message=request.POST["message"], email=request.POST["email"])
        nuevoformask.save()
        return render(request,"AppLacasona/inicio.html")
    
    return render(request, "AppLacasona/form_askanything.html")

def search_mailfornl(request):
    return render(request, "AppLacasona/search_mailfornl.html")

def view_mailfornl(request):

    if request.GET["email"]:

        email = request.GET["email"]
        all_emails = Newsletter.objects.filter(email__icontains=email)

        return render(request, "AppLacasona/view_mailfornl.html", {"all_emails": all_emails, "email":email})
    
    else:

        respuesta = "No estas suscrito al Newsletter."

    return HttpResponse(respuesta)





















"""""
def email_nl(request):
    emailnl = Newsletter(nombre="andres", apellido="lozano", email="andyxinvierno@gmail.com")
    emailnl.save()
    return HttpResponse(f"Te enviaremos información a {emailnl.email}")

def song_request(request):
    songrequest = SendSong(songname="Adios", deadline=20/20/2020)
    songrequest.save()
    return HttpResponse(f"Haz enviado tu canción {songrequest.songname}. Te enviaremos informacion de cuanto sale masterizarla antes de tu deadline {songrequest.deadline}")
"""""