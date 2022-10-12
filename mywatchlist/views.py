from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchlist
# Create your views here.

def show_watchlist(request):
    # queries the database
    data_wishlist = MyWatchlist.objects.all()
    
    # create dictionary for context
    context = {
            'watch_list' : data_wishlist
    }
    return render(request, 'mywatchlist.html',context)

def show_watchlist_xml(request):
    # queries the database
    data_wishlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml",data_wishlist),
     content_type="application/xml")

def show_watchlist_json(request):
    # queries the database
    data_wishlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json",data_wishlist),
     content_type="application/json")
