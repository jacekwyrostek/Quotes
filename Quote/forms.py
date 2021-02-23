from django.forms import ModelForm
from .models import *

class QuoteForm(ModelForm):
    class Meta:
        model=Quote
        exclude=[]

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        exclude=[]

class BookForm(ModelForm):
    class Meta:
        model=Book
        exclude=[]

class PubHouseForm(ModelForm):
    class Meta:
        model=PubHouse
        exclude=[]
