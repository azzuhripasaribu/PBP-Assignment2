from django.urls import path
from mywatchlist.views import show_watchlist,show_watchlist_xml,show_watchlist_json

app_name = 'mywatchlist'

urlpatterns = [
    path('html', show_watchlist, name='show_watchlist'),
    path('xml', show_watchlist_xml, name='show_watchlist_xml'),
    path('json', show_watchlist_json, name='show_watchlist_json'),
]