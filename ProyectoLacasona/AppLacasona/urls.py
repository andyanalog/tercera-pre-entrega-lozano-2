from django.urls import path
from .views import *

urlpatterns = [

    #url inicio
    path("inicio/", inicio, name="Inicio"),

    #urls leer
    path("newsletter/", newsletter, name="Newsletter"),
    path("sendsong/", sendsong, name="Sendsong"),
    path("askanything/", askanything, name="Askanything"),

    #urls de formularios
    path("form_newsletter/", form_mailfornl, name="FormNewsletter"),
    path("form_sendsong/", form_sendsong, name="FormSendSong"),
    path("form_askanything/", form_askanything, name="FormAskAnything"),

    #urls de búsqueda
    path("search_mailfornl/", search_mailfornl, name="SearchMailfornl"),
    path("view_mailfornl/", view_mailfornl, name="ViewMailfornl")
]