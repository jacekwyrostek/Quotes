from django.contrib import admin
from .models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['title', 'author']
    list_filter=()

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ordering=['surname', 'name']
    list_display=['surname', 'name', 'birth', 'death']

@admin.register(PubHouse)
class PubHouseAdmin(admin.ModelAdmin):
    list_display=['houseName']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display=['desc', 'date', 'author']
    list_filter=('author',)
