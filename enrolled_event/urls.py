from django.urls import path
from enrolled_event.views import show_enrolled_event

app_name = 'wishlist'

urlpatterns = [
    path('', show_enrolled_event, name='show_enrolled_event'),
]