from django.db import models
from django.core.validators import MaxLengthValidator

class PubHouse(models.Model):
    houseName=models.CharField(max_length=100, verbose_name=u"Publishing House:", unique=True)

    class Meta:
        ordering=['houseName']

    def __str__(self):
        return self.houseName

class Author(models.Model):
    surname=models.CharField(max_length=100, verbose_name=u"Surname:")
    name=models.CharField(max_length=100, verbose_name=u"Name:")
    birth=models.IntegerField(default=0000, blank=False, null=False, verbose_name=u"Birth Year:")
    death=models.IntegerField(default=0000, blank=False, null=False, verbose_name=u"Death Year:")

    class Meta:
        unique_together = ('surname', 'name')
        ordering=['surname', 'name']

    def __str__(self):
        return self.surname + ' ' + self.name + ' (' + str(self.birth) + '-' + str(self.death) + ')'

class Book(models.Model):
    title=models.CharField(max_length=100, verbose_name=u"Title:")
    author=models.ForeignKey(Author, null=True, on_delete=models.CASCADE, verbose_name=u"Author:")
    pubHouse=models.ForeignKey(PubHouse, null=True, on_delete=models.CASCADE, verbose_name=u"publishing House:")
    city=models.CharField(max_length=100, null=True, verbose_name=u"City:")
    pubYear=models.IntegerField(default=0000, blank=False, null=False, verbose_name=u"Publishing Year:")

    class Meta:
        unique_together = ('title', 'author')
        ordering = ['title']

    def __str__(self):
        return self.title

class Quote(models.Model):
    choice=[
        ('No','No'),
        ('Yes','Yes')
        ]
    desc=models.CharField(max_length=100, verbose_name=u"Description:")
    date=models.DateField(null=True, blank=True, verbose_name=u"Date of the Quote:", help_text="<em>YYYY-MM-DD</em>.")
    text=models.TextField(verbose_name=u"Quote Text:")
    page=models.PositiveSmallIntegerField(null=True, verbose_name=u"Page:")
    author=models.ForeignKey(Author, null=True, on_delete=models.CASCADE, verbose_name=u"Author:")
    book=models.ForeignKey(Book, null=True, on_delete=models.CASCADE, verbose_name=u"Book:")
    check=models.CharField(max_length=3, choices=choice, default='No')

    class Meta:
        ordering=['date']

    def __str__(self):
        return self.desc
