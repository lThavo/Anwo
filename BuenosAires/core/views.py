from django.shortcuts import redirect, render
from .models import Aire, Categoria
from .forms import AireForm
 
# Create your views here.
 
def home(request):
    return render(request, "core/home.html")
 
def aire_tienda(request):
    data = {"list": Aire.objects.all().order_by('codigo')}
    return render(request, "core/aire_tienda.html", data)
 
def aire_ficha(request, id):
    aire = Aire.objects.get(codigo=id)
    data = {"aire":  aire}
    return render(request, "core/aire_ficha.html", data)
 
def aire(request, action, id):
    data = {"mesg": "", "form": AireForm, "action": action, "id": id}
 
    if action == 'ins':
        if request.method == "POST":
            form = AireForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡El Aire Acondicionado fue creado correctamente!"
                except:
                    data["mesg"] = "¡No se puede crear dos Aires Acondicionados con el mismo codigo!"
 
    elif action == 'upd':
        objeto = Aire.objects.get(patente=id)
        if request.method == "POST":
            form = AireForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡El aire fue actualizado correctamente!"
        data["form"] = AireForm(instance=objeto)
 
    elif action == 'del':
        try:
            Aire.objects.get(patente=id).delete()
            data["mesg"] = "¡El aire fue eliminado correctamente!"
            return redirect(aire, action='ins', id = '-1')
        except:
            data["mesg"] = "¡El aire ya estaba eliminado!"
 
    data["list"] = Aire.objects.all().order_by('codigo')
    return render(request, "core/aire.html", data)


def poblar_bd(request):
    Aire.objects.all().delete()
    Aire.objects.create(codigo="ALAN67", tipo='MultiSplit', btu="16000", imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=1))
    Aire.objects.create(codigo="ALAN67", tipo='Portatil', btu="10000", imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=2))
    Aire.objects.create(codigo="ALAN67", tipo='Ventana', btu="5000", imagen="images/volvosw.jpg", categoria=Categoria.objects.get(idCategoria=3))
    return redirect(aire, action='ins', id = '-1')
