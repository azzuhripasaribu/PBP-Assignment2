from gettext import Catalog
from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_wishlist = CatalogItem.objects.all()
    context = {
            'name' : 'Azzuhri',
            'npm' : '2006489634',
            'list_item' : data_wishlist
    }
    return render(request, 'katalog.html',context)