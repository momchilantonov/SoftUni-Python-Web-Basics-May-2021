from django.shortcuts import render, redirect
from .forms import BookModelForm
from .models import Book


# Create your views here.
def show_book_form(req, form, temp):
    context = {
        'form': form,
    }
    return render(req, temp, context)


def save_book(req, form, red, temp):
    if form.is_valid():
        form.save()
        return redirect(red)
    return show_book_form(req, form, temp)


def index(req):
    context = {
        'books': Book.objects.all()
    }
    return render(req, "index.html", context)


def create_book(req):
    if req.method == 'GET':
        form = BookModelForm()
        return show_book_form(req, form, 'create.html')
    form = BookModelForm(req.POST)
    return save_book(req, form, 'index', 'create.html')


def edit_book(req, pk):
    book = Book.objects.get(pk=pk)
    if req.method == 'GET':
        form = BookModelForm(
            initial=book.__dict__,
        )
        return show_book_form(req, form, 'edit.html')
    form = BookModelForm(
        req.POST,
        instance=book,
    )
    return save_book(req, form, 'index', 'edit.html')
