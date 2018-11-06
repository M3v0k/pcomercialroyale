from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CartaForm
from royale.models import Carta, Tipo, Level

# Create your views here.
def lista_carta(request):
     carta = Carta.objects.all()
     return render(request, 'royale/carta_lista.html',{'carta':carta})

def detalle_carta(request,id):
     carta = get_object_or_404(Carta,id=id)
     level = Level.objects.all()
     tipo = Tipo.objects.all()
     return render(request,"royale/carta_detalle.html",{'carta':carta,'level':level,'tipo':tipo})

def carta_nuevo(request):
    if request.method == 'POST':
        formulario = CartaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Carta Guardada Exitosamente')
    else:
        formulario = CartaForm()
    return render(request, 'royale/carta_nuevo.html', {'formulario': formulario})
