from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Avatar, cliente, mecanico, reparacion
from blog.forms import AvatarFormulario, UserEditForm, clienteFormulario
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def inicio(request):
    try:
        avatar = Avatar.objects.get(user=request.user.id) 
        return render (request, "Bienvenida.html", {"url":avatar.imagen.url})
    except:
    
        return render (request, "Bienvenida.html")

    


def Cliente(request):

    return render(request, "clientes.html")


def EditaElimina(request):
    lista = cliente.objects.all()

    return render(request, "EditarEliminarCliente.html", {"lista_clientes": lista})


@staff_member_required(login_url='Login')
def mecanico(request):
    
    return render(request, "mecanicos.html")



def reparacion(request):

    return render(request, "Reparaciones.html")

    


def ClienteFormulario(request):

    print('method:', request.method)
    print('post:', request.POST)

    if request.method == 'POST':

        miFormulario = clienteFormulario(request.POST)
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            Cliente = cliente(nombre = data['nombre'], apellido= data ['apellido'], vehiculo=data['vehiculo'])
            Cliente.save()
            return render(request, "Bienvenida.html", {"mensaje": "Cliente cargado con exito"})

    else:
        miFormulario = clienteFormulario()

    return render(request, "clienteFormulario.html", {"miFormulario": miFormulario})



@login_required
def BusquedaCliente(request):

    return render(request, "BusquedaCliente.html")

def Buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        clientes = cliente.objects.filter(nombre__icontains=nombre)

        return render(request, "ResultadoBusqueda.html", {"cliente": clientes, "nombre": nombre})

    else:
        respuesta= "no enviaste datos"

    return HttpResponse(respuesta)  




def lista_clientes(self):

    lista = cliente.objects.all()
    
    return render(self, "lista_clientes.html", {"lista_clientes": lista})

    


def eliminarCliente (request, id):

    if request.method =="POST":

        clienteEliminado = cliente.objects.get(id=id)

        clienteEliminado.delete()

        lista = cliente.objects.all()

        return render(request, "lista_clientes.html", {"lista_clientes": lista})


def editarCliente (request, id):

    print('method:', request.method)
    print('post:', request.POST)

    clienteEditado = cliente.objects.get(id=id)


    if request.method == 'POST':

        miFormulario = clienteFormulario(request.POST)
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            clienteEditado.nombre = data["nombre"]
            clienteEditado.apellido = data["apellido"]
            clienteEditado.vehiculo= data["vehiculo"]
            
            clienteEditado.save()

            return render(request, "padre.html")

    else:
        miFormulario = clienteFormulario(initial= {
            "nombre": clienteEditado.nombre,
            "apellido": clienteEditado.apellido,
            "vehiculo": clienteEditado.vehiculo,
        })

    return render(request, "editarCliente.html", {"miFormulario": miFormulario, "id": clienteEditado.id})

class ClienteList (LoginRequiredMixin, ListView):

    model= cliente
    template_name = 'clientesList.html'



class ClienteDetail (DetailView):

    model= cliente
    template_name = 'clientesDetail.html'

class ClienteCreate (CreateView):

    model= cliente
    template_name = 'clientesCreate.html'
    fields = ["nombre", "apellido"]
    success_url = '/inicio/'

class ClienteUpdate (UpdateView):

    model= cliente
    template_name = 'clientesUpdate.html'
    fields = ('__all__')
    success_url = '/inicio/'

class ClienteDelete (DeleteView):

    model= cliente
    template_name = 'clientesDelete.html'
    success_url = '/inicio/'


def LoginView(request):
    
    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data
            usuario = data['username']
            psw = data['password']

            user = authenticate(username=usuario, password=psw)

            if user:
                login(request, user)

                return render(request, "Bienvenida.html", {"mensaje":f'Bienvenido {usuario}'})
            
            else:
                return render(request, "Bienvenida.html", {"mensaje": "Error datos incorrectos"})
            

        return render(request, "Bienvenida.html", {"mensaje": "Error formulario incorrecto"})

    else:
        miFormulario = AuthenticationForm()

    return render(request, "Login.html", {"miFormulario": miFormulario})



def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            username=  form.cleaned_data["username"]

            form.save()

            return render(request, "Bienvenida.html", {"mensaje": f'usuario {username} creado'})


    else:

        form = UserCreationForm()

    return render(request, "Registro.html", {"miFormulario": form})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid(): 

            data=miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
           
            
            usuario.save()
            
            return render(request, "Bienvenida.html", {"mensaje": "Datos actualizados con exito"})
        
    else:

        miFormulario = UserEditForm(instance=request.user)

    return render(request, "EditarPerfil.html", {"miFormulario": miFormulario})

def agregar_avatar(request):
    
    if request.method == 'POST':

        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():

            data=miFormulario.cleaned_data

            avatar = Avatar(user = request.user, imagen= data ['imagen'])
            avatar.save()
            return render(request, "Bienvenida.html", {"mensaje": "avatar cargado"})

    else:
        miFormulario = AvatarFormulario()

    return render(request, "CrearAvatar.html", {"miFormulario": miFormulario})


    
def EditarDatos(request):

    return render(request, "EditarDatos.html")