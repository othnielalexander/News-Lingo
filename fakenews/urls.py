from django.urls import path

from . import views

urlpatterns = [
    path('', views.fakenews, name='home')
]