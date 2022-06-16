from django.shortcuts import render, redirect
from django.template.defaulttags import url

from .forms import BookForm, ImageBookForm, PersonReaderForm, Author_form
from .models import Book, ImageBook


def page_index(request):
    form = BookForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            ImageBook.objects.create(photo_book=request.FILES['image'], books=book)
        else:
            erorr=form.errors
            context={
                'form':form,
                'error':erorr,
            }
    return render(request, 'page_index.html', context)


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
            erorr=form.errors
            context={
                'form':form,
                'error':erorr,
            }
    return render(request, 'image_add.html', context)


def main_page(request):
    return render(request, 'main_page.html')


def add_reader(request):
    form = PersonReaderForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = PersonReaderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            erorr=form.errors
            context={
                'form':form,
                'error':erorr,
            }
    return render(request, 'person_form.html', context)


def add_author(request):
    form = Author_form()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = Author_form(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            erorr=form.errors
            context={
                'form':form,
                'error':erorr,
            }
    return render(request, 'author_form.html', context)

def lending_book(request):
    return render(request, 'lending_book.html')

def book_return(request):
    return render(request, 'book_return.html')

def user_list(request):
    return render(request, 'user_list.html')

def search(request):
    return render(request, 'search.html')