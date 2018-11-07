from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import CartaForm, TipoForm
from royale.models import Carta, Tipo, Level
from django.contrib.auth.decorators import login_required


# Create your views here.
def lista_carta(request):
     carta = Carta.objects.all()
     return render(request, 'royale/carta_lista.html',{'carta':carta})


def detalle_carta(request,id):
     carta = get_object_or_404(Carta,id=id)
     level = Level.objects.all()
     tipo = Tipo.objects.all()
     return render(request,"royale/carta_detalle.html",{'carta':carta,'level':level,'tipo':tipo})

def detalle_tipo(request,id):
     tipo = get_object_or_404(Tipo,id=id)
     return render(request,"royale/tipo_detalle.html",{'tipo':tipo})

@login_required
def carta_nuevo(request):
    if request.method == 'POST':
        formulario = CartaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.add_message(request, messages.SUCCESS, 'Carta Guardada Exitosamente')
            return redirect('/')
    else:
        formulario = CartaForm()
    return render(request, 'royale/carta_nuevo.html', {'formulario': formulario})

@login_required
def carta_editar(request, id):
    carta = get_object_or_404(Carta, id=id)
    if request.method == "POST":
        formulario = CartaForm(request.POST, request.FILES, instance=carta)
        if formulario.is_valid():
            carta = formulario.save()
            carta.save()
            return redirect('detalle_carta', id=carta.id)
    else:
        formulario = CartaForm(instance=carta)
    return render(request, 'royale/carta_editar.html', {'formulario': formulario})

@login_required
def tipo_editar(request, id):
    tipo = get_object_or_404(Tipo, id=id)
    if request.method == "POST":
        formulario = TipoForm(request.POST, instance=tipo)
        if formulario.is_valid():
            tipos = formulario.save()
            tipos.save()
            return redirect('detalle_tipo', id=tipo.id)
    else:
        formulario = TipoForm(instance=tipo)
    return render(request, 'royale/tipo_editar.html', {'formulario': formulario})

@login_required
def carta_eliminar(request, id):
    carta = get_object_or_404(Carta, id=id).delete()
    return render(request, 'royale/carta_eliminar.html')

@login_required
def tipo_eliminar(request, id):
    tipo = get_object_or_404(Tipo, id=id).delete()
    return render(request, 'royale/tipo_eliminar.html')


@login_required
def tipo_nuevo(request):
    if request.method == 'POST':
        formtipo = TipoForm(request.POST)
        if formtipo.is_valid():
            formtipo.save()
            messages.add_message(request, messages.SUCCESS, 'Tipo Guardado Exitosamente')
    else:
        formtipo = TipoForm()
    return render(request, 'royale/tipo_nuevo.html', {'formtipo': formtipo})
