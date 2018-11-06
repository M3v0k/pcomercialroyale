from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.lista_carta, name ='lista_carta'),
    url(r'^carta/nuevo/$', views.carta_nuevo, name='carta_nuevo'),
    url(r'^carta/(?P<id>[0-9]+)/$', views.detalle_carta, name='detalle_carta'),
    ]
