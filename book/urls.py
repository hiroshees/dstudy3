from django.contrib import admin
from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
    path("book/list", views.BookListView.as_view() , name="book_list"),
    path('book/create', views.BookCreateView.as_view(), name='book_create'),
    path('book/edit/<int:pk>', views.BookEditView.as_view(), name='book_edit'),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),
    path('book/detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path("category/list", views.CategoryListView.as_view() , name="category_list"),
    path('category/create', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/edit/<int:pk>', views.CategoryEditView.as_view(), name='category_edit'),
    path("author/list", views.AuthorListView.as_view() , name="author_list"),
    path('author/create', views.AuthorCreateView.as_view(), name='author_create'),
    path('author/edit/<int:pk>', views.AuthorEditView.as_view(), name='author_edit'),
    path('author/detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
]
