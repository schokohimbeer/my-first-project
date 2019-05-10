from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

#aus der Datei Views, Funktion post_list