# capa de vista/presentación
# si se necesita algún dato (lista, valor, etc), esta capa SIEMPRE se comunica con services_nasa_image_gallery.py

from django.shortcuts import redirect, render
from .layers.services import services_nasa_image_gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# función que invoca al template del índice de la aplicación.
def index_page(request):
    return render(request, 'index.html')

def getAllImagesAndFavouriteList(request):
    images = services_nasa_image_gallery.getAllImages()
    #favourite_list = []

    return images#, favourite_list

def home(request):
    # llama a la función auxiliar getAllImagesAndFavouriteList() y obtiene 2 listados: uno de las imágenes de la API y otro de favoritos por usuario*.
    # (*) este último, solo si se desarrolló el opcional de favoritos; caso contrario, será un listado vacío [].
    images = getAllImagesAndFavouriteList(request)
    #favourite_list = []
    return render(request, 'home.html', {'images': images, } )#'favourite_list': favourite_list} )


def search(request):
    # images, favourite_list = getAllImagesAndFavouriteList(request)
    images = getAllImagesAndFavouriteList(request)
    search_msg = request.POST.get('query', '')
    if search_msg == "":
        return render (request, 'home.html', {'images': images } )
    else:
        busqueda = services_nasa_image_gallery.getImagesBySearchInputLike(search_msg)
        return render (request, 'home.html', {'images': busqueda } )


# las siguientes funciones se utilizan para implementar la sección de favoritos: traer los favoritos de un usuario, guardarlos, eliminarlos y desloguearse de la app.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', {'favourite_list': favourite_list})


@login_required
def saveFavourite(request):
    pass


@login_required
def deleteFavourite(request):
    pass


@login_required
def exit(request):
    return home(request)