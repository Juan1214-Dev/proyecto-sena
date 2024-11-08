from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from tienda.models import Producto
from .models import Usuario
from .models import Padre
from .models import Ninoabuelo
from .models import Pago
from django.contrib import messages




def login(request):
    if request.method == "POST":
        usuario = request.POST.get("nick")
        clave = request.POST.get("password")

        try:
            q = Usuario.objects.get(nick=usuario, password=clave)
            messages.success(request, "Bienvenido!!")
            # Guardar nombre del rol  y no su número
            datos = {
                "rol": q.rol,
                "nombre_rol": q.get_rol_display(),
                "nombre": f"{q.nombre} {q.apellido}",
                "id": q.id
            }
            request.session["logueo"] = datos

            return HttpResponseRedirect(reverse("plantilla.html"))

        except Usuario.DoesNotExist:
            messages.error(request, "Usuario o contraseña no válidos..")

            return render(request, "login.html")
    else:

        if request.session.get("logueo", False):
            return HttpResponseRedirect(reverse("plantilla.html"))
        else:
            return render(request, "login.html")


def logout(request):
    try:
        del request.session["logueo"]
        messages.success(request, "Sesión cerrada correctamente!")
    except Exception as e:
        messages.error(request, f"Error: {e} ")
    return HttpResponseRedirect(reverse("login"))


def cambiar_clave(request):
    return render(request, "tienda/usuarios/cambio_clave.html")


def ver_perfil(request):
    return render(request, "tienda/usuarios/perfil.html")

def guardar_clave(request):
    usuario = request.session.get("logueo", False)

    if usuario:
        if request.method == "POST":
            actual = request.POST.get("actual")
            clave1 = request.POST.get("clave1")
            clave2 = request.POST.get("clave2")

            try:
                q = usuario.objects.get(pk=usuario["id"], passwd=actual)
                if clave1 == clave2:
                    q.passwd = clave1
                else:
                    messages.warning(request, "Nuevas contraseñas no coinciden...")
                    return  HttpResponseRedirect(reverse("tienda:cambiar_clave" , kwargs={actual:actual}))
            except Exception as e:
                messages.warning(request, "Contraseña no válida...")

            return HttpResponseRedirect(reverse("tienda:cambiar_clave"))

    else:
        return HttpResponseRedirect(reverse("tienda:login"))


# Create your views here.

def home(request):
    return render(request,"principal.html")

def consultar(request):
    productos = Producto.objects.all()
    return render(request,"productos.html",{
        'productos' : productos
    })

def guardar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    p = Producto(nombre = nombre, precio = precio, descripcion = descripcion)
    p.save()
    messages.success(request, 'Producto agregado')
    return redirect('consultar')

def eliminar(request, id):
    producto = Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request,'Producto eliminado')
    return redirect('consultar')

def detalle(request, id):
    producto = Producto.objects.get(pk=id)
    return render(request, "productoEditar.html",{
        'producto' : producto
    })

def editar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    id = request.POST["id"]
    Producto.objects.filter(pk=id).update(id=id, nombre=nombre, precio=precio, descripcion=descripcion)
    messages.success(request,'Producto actualizado')
    return redirect('consultar')

############Aqui comienza el modulo de Usuarios######################################


def usuarios(request):

    usuarios = Usuario.objects.all()
    return render(request, "usuarios.html", {
        'usuarios': usuarios
    })

#Quiero recordar que en esta parte se agrego el nick y el rol, teniendo encuenta la migracion#
def guardar_usuario(request):
    nombre = request.POST.get("nombre")
    apellido = request.POST.get("apellido")
    nick = request.POST.get("nick")
    correo = request.POST.get("correo")
    rol = request.POST.get("rol")
    password = request.POST.get("password")
    
    descripcion = request.POST.get("descripcion")
    try: 
        p = Usuario(nombre = nombre, apellido = apellido, nick = nick  ,correo = correo, password = password, rol = rol ,descripcion = descripcion)
        p.save()
        messages.success(request, 'usuarios agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')
      

    return redirect('usuarios')

def eliminar_usuario(request, id):
    usuario = Usuario.objects.filter(pk=id)
    try:
        usuario.delete()
        messages.success(request,'Usuario eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('usuarios')

def detalle_usuario(request, id):
    usuario = Usuario.objects.get(pk=id)
    return render(request, "usuarioEditar.html",{
        'usuarios' : usuario
    })

def editar_usuario(request):
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        nick = request.POST.get("nick")
        correo = request.POST.get("correo")
        password = request.POST.get("password")
        rol = request.POST.get("rol")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Usuario.objects.filter(pk=id).update(id=id,nombre = nombre, apellido = apellido, nick = nick ,correo = correo, password = password, rol = rol, descripcion = descripcion )
        try:
            messages.success(request,'Usuario actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('usuarios')

##### Aqui termina el modulo de usuarios #######################################

def padres(request):

    padres = Padre.objects.all()
    return render(request, "padres.html", {
        'padres': padres
    })

def guardar_padres(request):
    nombre = request.POST.get("nombre")
    genero = request.POST.get("genero")
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    email = request.POST.get("email")
    telefono = request.POST.get("telefono")
    direccion = request.POST.get("direccion")
    descripcion = request.POST.get("descripcion")
    try: 
        p = Padre(nombre = nombre, genero = genero, fecha_nacimiento = fecha_nacimiento, email = email, telefono = telefono, direccion = direccion, descripcion = descripcion)
        p.save()
        messages.success(request, 'Padre agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')
      
      
    return redirect('padres')

def eliminar_padres(request, id):
    padre = Padre.objects.filter(pk=id)
    try:
        padre.delete()
        messages.success(request,'Padre eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('padres')

def detalle_padres(request, id):
    padre = Padre.objects.get(pk=id)
    return render(request, "padreEditar.html",{
        'padres' : padre
    })

def editar_padres(request):
        nombre = request.POST.get("nombre")
        genero = request.POST.get("genero")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        direccion = request.POST.get("direccion")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Padre.objects.filter(pk=id).update(id=id,nombre = nombre, genero = genero, fecha_nacimiento = fecha_nacimiento, email = email, telefono = telefono, direccion = direccion, descripcion = descripcion )
        try:
            messages.success(request,'Padre actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('padres')

###########################################################################################

def ninoabuelos(request):

    ninoabuelos = Ninoabuelo.objects.all()
    return render(request, "ninoabuelos.html", {
        'ninoabuelos': ninoabuelos
    })

def guardar_ninoabuelos(request):
    nombre = request.POST.get("nombre")
    fecha_nacimiento = request.POST.get("fecha_nacimiento")
    numero_identificacion = request.POST.get("numero_identificacion")
    descripcion = request.POST.get("descripcion")
    try: 
        p = Ninoabuelo(nombre = nombre, fecha_nacimiento = fecha_nacimiento, numero_identificacion = numero_identificacion,  descripcion = descripcion)
        p.save()
        messages.success(request, 'Niño/Abuelo agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')

    return redirect('ninoabuelos')

def eliminar_ninoabuelos(request, id):
    ninoabuelo = Ninoabuelo.objects.filter(pk=id)
    try:
        ninoabuelo.delete()
        messages.success(request,'Niño/Abuelo eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('ninoabuelos')

def detalle_ninoabuelos(request, id):
    ninoabuelo = Ninoabuelo.objects.get(pk=id)
    return render(request, "ninoabueloEditar.html",{
        'ninoabuelos' : ninoabuelo
    })

def editar_ninoabuelos(request):
        nombre = request.POST.get("nombre")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        numero_identificacion = request.POST.get("numero_identificacion")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Ninoabuelo.objects.filter(pk=id).update(id=id,nombre = nombre, fecha_nacimiento = fecha_nacimiento, numero_identificacion = numero_identificacion,  descripcion = descripcion )
        try:
            messages.success(request,'Niños/Abuelo actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('ninoabuelos')

###########################################################################################

def pagos(request):

    pagos = Pago.objects.all()
    return render(request, "pagos.html", {
        'pagos': pagos
    })

def guardar_pagos(request):
    monto = request.POST.get("monto")
    fecha_pago = request.POST.get("fecha_pago")
    metodo_pago = request.POST.get("metodo_pago")
    descripcion = request.POST.get("descripcion")
    try: 
        p = Pago(monto = monto, fecha_pago = fecha_pago, metodo_pago = metodo_pago, descripcion = descripcion)
        p.save()
        messages.success(request, 'Pago agregado')

    except Exception as e:
        messages.error(request, f'Error:{e}')
      
      
    return redirect('pagos')

def eliminar_pagos(request, id):
    pago = Pago.objects.filter(pk=id)
    try:
        pago.delete()
        messages.success(request,'Niño/Abuelo eliminado')
    except Exception as e :
        messages.error(request, f"Error: {e}")

    return redirect('pagos')

def detalle_pagos(request, id):
    pago = Pago.objects.get(pk=id)
    return render(request, "pagoEditar.html",{
        'pagos' : pago
    })

def editar_pagos(request):
        monto = request.POST.get("monto")
        fecha_pago = request.POST.get("fecha_pago")
        metodo_pago = request.POST.get("metodo_pago")
        descripcion = request.POST.get("descripcion")
        id = request.POST.get("id")
        Pago.objects.filter(pk=id).update(id=id, monto = monto, fecha_pago = fecha_pago, metodo_pago = metodo_pago,  descripcion = descripcion )
        try:
            messages.success(request,'Pago actualizado')
        except Exception as e:
            messages.error( request, f"Error: {e}")

        return redirect('pagos')