from django.urls import path
from blog.views import Cliente, ClienteCreate, ClienteDelete, ClienteDetail, ClienteList, EditaElimina, EditarDatos, LoginView, agregar_avatar, cliente, editar_perfil, editarCliente, eliminarCliente, lista_clientes, mecanico, BusquedaCliente, ClienteFormulario, register, reparacion, inicio, Buscar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    path('cliente/', Cliente, name ='cliente'),
    path('mecanico/', mecanico, name="mecanico"),
    path('reparaciones/', reparacion, name= "reparaciones"),
    path('clienteFormulario/',ClienteFormulario, name="clienteFormulario" ),
    path('buscarcliente/', BusquedaCliente, name="BusquedaCliente" ),
    path('buscar/', Buscar , name ="Buscar" ), 
    path('lista-clientes/', lista_clientes, name ="lista" ), 
    path('eliminacliente/<int:id>', eliminarCliente, name ="eliminaCliente" ), 
    path('editaCliente/<int:id>', editarCliente, name ="editarCliente" ), 
    path('clientelist', ClienteList.as_view(), name ="clientelist" ),
    path('detailcliente/<int:pk>', ClienteDetail.as_view(), name ="clientesDetail" ),  
    path('CreaCliente/', ClienteCreate.as_view(), name ="CreaCliente" ),  
    path('EliminarCliente/<int:pk>', ClienteDelete.as_view(), name ="EliminarCliente" ),  
    path('login/', LoginView, name ="Login" ),  
    path('registro/', register, name ="Registrar" ),  
    path('logout/', LogoutView.as_view(template_name='logout.html'), name ="Logout" ),  
    path('editar-perfil/', editar_perfil, name ="EditarPerfil" ), 
    path('agregar-avatar/', agregar_avatar, name ="CrearAvatar" ),  
    path('editar-datos/', EditarDatos, name ="EditarDatos" ),  
    path('EditaEliminaCliente/', EditaElimina, name ="EditaEliminaCliente" ), 





    
]
