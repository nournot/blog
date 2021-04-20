from django.urls import path
from . import views
from .views import LinkListView

app_name = 'config'

urlpatterns = [
    path('links/', LinkListView.as_view(), name='links')
    # path('links/', views.links, name='links')
]