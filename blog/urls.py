from django.urls import path
from .views import (
    article_list,
    article_detail,
    article_create,
    article_update,
    article_delete,
)

urlpatterns = [
    path("blog/", article_list, name="article_list"),
    path("blog/article/<int:pk>/", article_detail, name="article_detail"),
    path("blog/article/new/", article_create, name="article_create"),
    path("blog/article/<int:pk>/edit/", article_update, name="article_update"),
    path("blog/article/<int:pk>/delete/", article_delete, name="article_delete"),
]
