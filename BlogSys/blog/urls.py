from django.urls import path

from . import views
from .views import (
    IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView,
)


app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='post_list'),
    path('category/<category_id>/', CategoryView.as_view(), name='post_list_for_category'),
    path('tag/<tag_id>/', TagView.as_view(), name='post_list_for_tag'),
    path('post/<pk>.html', PostDetailView.as_view(), name='detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<owner_id>/', AuthorView.as_view(), name='author'),

    # path('', views.post_list, name='post_list'),
    # path('post/<post_id>.html',views.detail, name='detail'),
    # path('category/<category_id>/', views.post_list, name='post_list_for_category'),
    # path('tag/<tag_id>/', views.post_list, name='post_list_for_tag'),
]