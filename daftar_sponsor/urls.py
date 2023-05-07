from django.urls import path
from daftar_sponsor.views import show_daftar_sponsor

app_name = 'wishlist'

urlpatterns = [
    path('', show_daftar_sponsor, name='show_daftar_sponsor'),
]