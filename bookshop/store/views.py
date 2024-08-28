from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category, Author, Rental
from django.contrib.auth.decorators import login_required

def book_list(request):
    books = Book.objects.filter(available=True)
    categories = Category.objects.all()
    authors = Author.objects.all()

    # Фильтрация по категории
    category_id = request.GET.get('category')
    if category_id:
        books = books.filter(category_id=category_id)

    # Фильтрация по автору
    author_id = request.GET.get('author')
    if author_id:
        books = books.filter(author_id=author_id)

    # Сортировка по году
    sort_by_year = request.GET.get('sort_by_year')
    if sort_by_year == 'asc':
        books = books.order_by('year')
    elif sort_by_year == 'desc':
        books = books.order_by('-year')

    return render(request, 'store/book_list.html', {
        'books': books,
        'categories': categories,
        'authors': authors,
    })

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        rental_period = request.POST.get('rental_period')
        Rental.objects.create(user=request.user, book=book, rental_period=rental_period)
        return redirect('book_list')
    return render(request, 'store/book_detail.html', {'book': book})
