from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/',views.detail, name='detail'),
    path('category/<category_id>/', views.post_list, name='post_list'),
    path('tag/<tag_id>/', views.post_list, name='post_list'),
]