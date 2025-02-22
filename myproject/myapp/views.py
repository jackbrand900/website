from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
from django.http import HttpResponse
from .models import Book

def add_example_book(request):
    title = "The Great Gatsby"
    author = "F. Scott Fitzgerald"
    published_date = "1925-04-10"
    
    # Check if a book with the same title and author already exists
    if Book.objects.filter(title=title, author=author).exists():
        return HttpResponse("Book already exists!")
    else:
        example_book = Book.objects.create(
            title=title,
            author=author,
            published_date=published_date
        )
        return HttpResponse(f"Added book: {example_book.title} by {example_book.author}")

def delete_book(request, pk):
    # Retrieve the book; if not found, return a 404 error
    book = get_object_or_404(Book, pk=pk)
    
    # Delete the book
    book.delete()
    
    # Optionally, redirect to a book list page or return a simple response
    return HttpResponse(f"Deleted book: {book.title}")