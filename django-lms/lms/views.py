from django.shortcuts import get_object_or_404, redirect, render
from .models import Book, Author, Customer, Genre, Checked_Out


def index(request):
    registered_books = Book.objects.all()
    context = {
        'books': registered_books
    }
    return render(request, 'lms/index.html', context)


def add_customer(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        customer = Customer.objects.create(name=name)
        
        return redirect('add_customer')
    else:
        return render(request, 'lms/add_customer.html', {'customers': Customer.objects.all()})


def checked_out_book(request):
    if request.method == 'POST':

        book_id = request.POST.get('book')
        customer_id = request.POST.get('customer')
        
        checked_out_book = Checked_Out.objects.create(book_id=book_id, customer_id=customer_id)
        
        return redirect('checked_out_book')
    else:
        return render(request, 'lms/checked_out_book.html', {'checked_out_books': Checked_Out.objects.all(), 'books': Book.objects.all(), 'customers': Customer.objects.all()})


def add_author(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        author = Author.objects.create(name=name)
        
        return redirect('add_author')
    else:
        return render(request, 'lms/add_author.html', {'authors': Author.objects.all()})


def add_genre(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        genre = Genre.objects.create(name=name)
        
        return redirect('add_genre')
    else:
        return render(request, 'lms/add_genre.html', {'genres': Genre.objects.all()})


def add_book(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        author_id = request.POST.get('author')
        genre_id = request.POST.get('genre')
        description = request.POST.get('description')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')

        author = Author.objects.get(id=author_id)
        genre = Genre.objects.get(id=genre_id)

        book = Book.objects.create(
            title=title,
            author=author,
            genre=genre,
            description=description,
            published_date=published_date,
            isbn=isbn
        )

        return redirect('lms-home')
    else:
        return render(request, 'lms/add_book.html', {'books': Book.objects.all(), 'authors': Author.objects.all(), 'genres': Genre.objects.all()})
    

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('lms-home')
    return redirect('lms-home')


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        author.delete()
        return redirect('add_author')
    return redirect('add_author')


def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    if request.method == 'POST':
        genre.delete()
        return redirect('add_genre')
    return redirect('add_genre')


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('add_customer')
    return redirect('add_customer')


def delete_checked_out(request, checked_out_id):
    checked_out = get_object_or_404(Checked_Out, pk=checked_out_id)
    if request.method == 'POST':
        checked_out.delete()
        return redirect('checked_out_book')
    return redirect('checked_out_book') 