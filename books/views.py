from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from books.models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'bla.html', {
        'books': books,
    })
