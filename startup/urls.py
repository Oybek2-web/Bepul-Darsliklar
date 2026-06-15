from django.urls import path
from . import views

app_name = 'startup'

urlpatterns = [
    path('', views.startup_list, name='startup_list'),
    path('startup_create/', views.startup_create, name='startup_create'),
    path('startup_update/<int:id>/', views.startup_update, name='startup_update'),
    path('startup_delete/<int:id>/', views.startup_delete, name='startup_delete'),
    path('startup_detail/<int:id>/', views.startup_detail, name='startup_detail')
]
