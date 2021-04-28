from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from datetime import datetime
import datetime, time, calendar
from django.contrib.auth.decorators import login_required

def StartView(request):
    quote=Quote.objects.order_by('?').first()
    obj={
        'quote':quote,
        }
    return render(request, 'start.html', obj)

def AuthorsView(request):
    quoteSource=Author.objects.all().order_by('surname', 'name')
    linkName='author'
    heading='Authors'
    editUrl='editAuthor'
    obj={
        'quoteSource':quoteSource,
        'linkName':linkName,
        'heading':heading,
        'editUrl':editUrl
        }
    return render(request, 'list.html', obj)

def AuthorView(request, id):
    quoteSource=Author.objects.get(pk=id)
    quote=Quote.objects.filter(author=quoteSource).order_by('date')
    obj={
        'quoteSource':quoteSource,
        'quote':quote,
        }
    return render(request, 'quotes.html', obj)

def BooksView(request):
    quoteSource=Book.objects.all().order_by('title')
    linkName='book'
    heading='Books'
    editUrl='editBook'
    obj={
        'quoteSource':quoteSource,
        'linkName':linkName,
        'heading':heading,
        'editUrl':editUrl
        }
    return render(request, 'list.html', obj)

def BookView(request, id):
    quoteSource=Book.objects.get(pk=id)
    quote=Quote.objects.filter(book=quoteSource)
    obj={
        'quoteSource':quoteSource,
        'quote':quote,
        }
    return render(request, 'quotes.html', obj)

def MonthView(request, month):
    quote=Quote.objects.filter(date__month=month).order_by('date__day')
    obj={
        'quote':quote,
    }
    return render(request, 'quotes.html', obj)

def ThisMonthView(request):
    month=datetime.datetime.today().month
    quote=Quote.objects.filter(date__month=month).order_by('date__day')
    obj={
        'quote':quote,
    }
    return render(request, 'quotes.html', obj)

@login_required
def NewQuote(request):
    form=QuoteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(StartView)
    obj={
        'form':form,
    }
    return render(request, 'form.html', obj)

@login_required
def NewAuthor(request):
    form=AuthorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(StartView)
    obj={
        'form':form,
    }
    return render(request, 'form.html', obj)

@login_required
def NewBook(request):
    form=BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(StartView)
    obj={
        'form':form,
    }
    return render(request, 'form.html', obj)

@login_required
def NewPubHouse(request):
    form=PubHouseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect(StartView)
    obj={
        'form':form,
    }
    return render(request, 'form.html', obj)

@login_required
def EditQuote(request, id):
    quote=get_object_or_404(Quote, pk=id)
    form=QuoteForm(request.POST or None, request.FILES or None, instance=quote)
    if form.is_valid():
        form.save()
        return redirect(StartView)
    obj={
        'form':form,
    }
    return render(request, 'form.html', obj)

@login_required
def EditAuthor(request, id):
    author=get_object_or_404(Author, pk=id)
    form=AuthorForm(request.POST or None, request.FILES or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect(StartView)
    obj={
        'form':form,
    }
    return render(request, 'form.html', obj)

@login_required
def EditBook(request, id):
    book=get_object_or_404(Book, pk=id)
    form=BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect(StartView)
    obj={
        'form':form,
    }
    return render(request, 'form.html', obj)

@login_required
def DeleteQuote(request, id):
    quote=get_object_or_404(Quote, pk=id)
    if request.method == 'POST':
        quote.delete()
        return redirect(StartView)
    obj={
        'quote':quote,
    }
    return render(request, 'delete.html', obj)
