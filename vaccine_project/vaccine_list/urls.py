from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_vaccine/', views.add_vaccine, name='add_vaccine')
]