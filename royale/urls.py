from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.lista_carta, name ='lista_carta'),
    url(r'^carta/nuevo/$', views.carta_nuevo, name='carta_nuevo'),
    url(r'^carta/(?P<id>[0-9]+)/$', views.detalle_carta, name='detalle_carta'),
    url(r'^tipo/nuevo/$', views.tipo_nuevo, name='tipo_nuevo'),
    url(r'^tipo/(?P<id>[0-9]+)/$', views.detalle_tipo, name='detalle_tipo'),
    url(r'^carta/(?P<id>[0-9]+)/edit/$', views.carta_editar, name='carta_editar'),
    url(r'^carta/(?P<id>[0-9]+)/delete/$', views.carta_eliminar, name='carta_eliminar'),

    ]
