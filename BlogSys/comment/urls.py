from django.urls import path

from . import views
from .views import CommentView

app_name = 'comment'

urlpatterns = [
    path('', CommentView.as_view(), name='comment'),
    # path('', views.comment_list, name='comment_list'),
]
