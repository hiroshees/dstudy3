from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import resolve_url
from django.http import HttpResponse
from django.http import Http404, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.conf import settings
from django.template.loader import render_to_string

from .models import Book, Author, Category
from .forms import BookUpdateForm


class BookListView(ListView):
    model = Book
    template_name = "book/book/list.html"
    

class BookCreateView(SuccessMessageMixin, CreateView):
    model = Book
    fields = ["title", "price", "author","category"]
    template_name = "book/book/create.html"
    success_url = reverse_lazy("book:book_list")
    success_message = "新規作成しました"
    
    def post(self, request, *args, **kwargs):
        """
        POSTメソッドで強引にエラーを設定する方法
        """
        self.object = Book()
        form = self.get_form()
        if int(form.data["price"]) <= 0 :
            form.add_error("price", "0円以上を入力してください")
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BookEditView(SuccessMessageMixin, UpdateView):
    """
    これはViewだけの方法
    """
    """
    model = Book
    fields = ["title", "price", "author","category"]
    template_name = "book/book/edit.html"
    success_url = reverse_lazy("book:book_list")
    success_message = "更新しました"
    """
    
    """
    これはフォームを利用する方法
    """
    model = Book
    form_class = BookUpdateForm
    template_name = "book/book/edit.html"
    success_url = reverse_lazy("book:book_list")
    success_message = "更新しました"


class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("book:book_list")
    
    def get(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        Book.objects.get(id=pk).delete()
        messages.success(self.request, "削除しました")
        return redirect(self.success_url)


class BookDetailView(DetailView):
    model = Book
    template_name = "book/book/detail.html"


class CategoryListView(ListView):
    model = Category
    template_name = "book/category/list.html"
    

class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name"]
    template_name = "book/category/create.html"
    success_url = reverse_lazy("book:category_list")
    success_message = "新規作成しました"


class CategoryEditView(SuccessMessageMixin, UpdateView):
    model = Category
    fields = ["name"]
    template_name = "book/category/edit.html"
    success_url = reverse_lazy("book:category_list")
    success_message = "更新しました"


class AuthorListView(ListView):
    model = Author
    template_name = "book/author/list.html"
    

class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    fields = ["name"]
    template_name = "book/author/create.html"
    success_url = reverse_lazy("book:author_list")
    success_message = "新規作成しました"


class AuthorEditView(SuccessMessageMixin, UpdateView):
    model = Author
    fields = ["name"]
    template_name = "book/author/edit.html"
    success_url = reverse_lazy("book:author_list")
    success_message = "更新しました"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "book/author/detail.html"

