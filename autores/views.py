from django.shortcuts import render
from django.http import HttpResponse

from autores.models import Autor

from django.views import View

# Create your views here.

# VISTAS TIPO FUNCIONES

def mi_vista(request):
    autor = Autor.objects.get(id=2)
    html = f'<html><body><h1>Hola mundo, {autor.nombre}</h1></body></html>'

    return HttpResponse(html)

def mostrar_autores(request):
    if request.method == 'POST':
        autor = request.POST
        Autor.objects.create(nombre=autor['nombre'], nacionalidad=autor['nacionalidad'], fecha_nacimeinto=autor['fecha_nacimiento'])

    autores = Autor.objects.all()
    contexto = {
        "autores": autores
    }
 
    return render(request, 'autores/lista.html', contexto)

#  VISTAS TIPO CLASES

def autor_id(request, id):
    try: 
        autor = Autor.objects.get(id=id)
        contexto = {
            "autor": autor
        }

        return render(request, 'autores/detalle.html', contexto)
    
    except:
        return render(request, 'autores/noAutor.html', {"id":id})


class AutoresView(View):
    http_method_names = ['post', 'get']

    def get(self, request):
        autores = Autor.objects.all()
        contexto = {
            "autores": autores
        }
    
        return render(request, 'autores/lista.html', contexto)

    def post(self, request):

        Autor.objects.create(
            nombre=request.POST['nombre'], 
            nacionalidad=request.POST['nacionalidad'], 
            fecha_nacimeinto=request.POST['fecha_nacimiento']
        )
        return self.get(request)


class AutorDetails(View):
    http_method_names = ['get']

    def get(self, request, id):
        try: 
            autor = Autor.objects.get(id=id)
            libros = autor.libros.all()
            contexto = {
                "autor": autor,
                "libros": libros
            }

            return render(request, 'autores/detalle.html', contexto)
        
        except:
            return render(request, 'autores/noAutor.html', {"id":id})