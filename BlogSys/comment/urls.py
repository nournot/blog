from django.urls import path

from . import views

app_name = 'comment'

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
]
