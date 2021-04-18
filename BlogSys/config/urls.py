from django.urls import path
from . import views

app_name = 'config'

urlpatterns = [
    path('links/', views.links, name='links')
]