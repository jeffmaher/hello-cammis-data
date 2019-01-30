from django.urls import path

from . import views

urlpatterns = [
    path('hello/<slug:name>', views.hello, name='hello'),
    path('add_greeting/<slug:name>', views.add_greeting, name='add_greeting'),
    path('alive', views.alive, name='alive'),
    path('ready', views.ready, name='ready'),
]