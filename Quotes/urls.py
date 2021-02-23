"""Quotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Quote.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('start/', StartView, name='start'),
    path('authors/', AuthorsView, name='authors'),
    path('authors/<int:id>', AuthorView, name='author'),
    path('books/', BooksView, name='books'),
    path('books/<int:id>', BookView, name='book'),
    path('month/<str:month>', MonthView, name='month'),
    path('this_month/', ThisMonthView, name='thisMonth'),

    path('newQoute/', NewQuote, name='newQuote'),
    path('newAuthor/', NewAuthor, name='newAuthor'),
    path('newBook/', NewBook, name='newBook'),
    path('newPubHouse/', NewPubHouse, name='newPubHouse'),

    path('editQuote/<int:id>', EditQuote, name='editQuote'),
    path('editAuthor/<int:id>', EditAuthor, name='editAuthor'),
    path('editBook/<int:id>', EditBook, name='editBook'),

    path('deleteQuote/<int:id>', DeleteQuote, name='deleteQuote'),
]
