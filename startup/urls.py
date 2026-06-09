from django.urls import path
from . import views

urlpatterns = [
    path('', views.startup_list, name='startup_list'),
    path('startup_create/', views.startup_create, name='startup_create')
]
