from django.shortcuts import render
from .models import Book

def books_list(request):
    list_of_books= Book.objects.all()
    context = { "books": list_of_books,
               }
    return render(request, "books/books_list.html", context)
