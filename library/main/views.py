import datetime

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView

from .forms import BookForm, ImageBookForm, PersonReaderForm, Author_form, BookFormGenre, BookFormAuthors

from .models import Book, ImageBook, PersonReader

from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    template_name = 'main_page.html'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Book.objects.get'
        return context


class GetDiscriptionBook(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ОписаниеКниги'
        return context


def page_index(request):
    form = BookForm()
    form_genre = BookFormGenre()
    form_authors = BookFormAuthors()
    context = {
        'form': form,
        'form_genre': form_genre,
        'form_authors': form_authors
    }
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            ImageBook.objects.create(photo_book=request.FILES['image'], books=book)
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
            }
    return render(request, 'page_index.html', context)


def book_genre_popup_add(request):
    if request.method == 'POST':
        form1 = BookFormGenre(request.POST)
        if form1.is_valid():
            form1.save()

    return redirect('lib:page_index')


def book_author_popup_add(request):
    if request.method == 'POST':
        form1 = BookFormAuthors(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
    return redirect('lib:page_index')


def image_add(request):
    form = ImageBookForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ImageBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
            }
    return render(request, 'image_add.html', context)


'''Не удалять и не коментить, сделал на ListView(эксперимент)'''


def main_page(request):
    books = Book.objects.all()
    paginator = Paginator(books, 1)
    page_number = request.GET.get('page', 1)
    title = 'Гавная страница'
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    return render(request, 'main_page.html', {'page_obj': page_obj, 'title': title})


def add_reader(request):
    form = PersonReaderForm()

    context = {
        'form': form,
        'title': 'Добавление читателя',
    }
    if request.method == 'POST':
        form = PersonReaderForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
                'title': 'Добавление читателя',
            }
    return render(request, 'person_form.html', context)


def add_author(request):
    form = Author_form()
    context = {
        'form': form,
        'title': 'Добавление автора',
    }
    if request.method == 'POST':
        form = Author_form(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            erorr = form.errors
            context = {
                'form': form,
                'error': erorr,
                'title': 'Добавление автора',
            }
    return render(request, 'author_form.html', context)


def readers_page(request):
    readers = PersonReader.objects.all()
    paginator = Paginator(readers, 1)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {
        'readers':readers,
        'title': 'Читатели',
        'page_obj': page_obj,
    }
    return render(request, 'reades_page.html', context)


def search_result(request):
    if request.method == 'GET':
        search= request.GET['search'].casefold()
        result= Book.objects.filter(name_book_rus=search)
        context={
            'book':result,
            'title':'поиск',
        }

        return render(request, 'search.html', context)


def give_book(request):
    readers = PersonReader.objects.all()
    context = {
        'readers': readers
    }
    return render(request, 'give_book.html', context)


def give_book_to_person(request, pk):
    books = Book.objects.all()
    context = {
        'books': books
    }
    reader = PersonReader.objects.get(pk=pk)
    # print(datetime.datetime.date(datetime.datetime.now()))
    if request.method == 'POST':
        if reader.book_set.all().exists():
            context = {
                'books': books,
                'error': 'данный читатель не сдал прошлые книги'
            }
        else:
            book=request.POST.getlist('books')
            if len(book) < 5 and len(book) > 0:

                for f in book:
                    reader.book_set.add(Book.objects.get(name_book_rus=f))
                reader.person_get_book=datetime.datetime.date(datetime.datetime.now())
                reader.save()
            else:
                context = {
                    'books': books,
                    'error': 'введите корректное число книг'
                }
    return render(request, 'book_to_reader.html', context)


def return_book(request):
    names = set(PersonReader.objects.filter(book__book_read_person__isnull=False))
    context = {
        'names': names,
        'title':'Список читателей',
    }
    return render(request, 'return_book.html', context)


def return_book_to_biblio(request, pk):
    reader = PersonReader.objects.get(pk=pk)
    books = reader.book_set.all()
    context = {
        'reader':reader,
        'books':books,
        'title':'СписокКниг',
    }
    # if request.method == 'POST':
        # if len(request.POST) > 1:

    return render(request, 'return_book_to_biblio.html', context)