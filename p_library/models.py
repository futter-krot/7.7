from django.db import models
from django.contrib.auth.models import User  
# Create your models here.
class Author(models.Model):  
    full_name = models.TextField()  
    birth_year = models.SmallIntegerField()  
    country = models.CharField(max_length=2)
    def __str__(self):
        return self.full_name
class Redaction(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):  
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()  
    description = models.TextField()  
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    copy_count = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    redaction = models.ForeignKey(Redaction, on_delete=models.CASCADE, null=True, blank=True, related_name='books')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    age = models.SmallIntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

# from django.db import models  


# class Book(models.Model):  
#     ISBN = models.CharField(max_length=13)  
#     title = models.TextField()  
#     description = models.TextField()  
#     year_release = models.SmallIntegerField()  
#     author = models.ForeignKey('Author', on_delete=models.CASCADE)
#     copy_count = models.IntegerField(default=1)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     redaction = models.ForeignKey('Redaction', on_delete=models.CASCADE, null=True, blank=True, related_name='books')

#     def __str__(self):
#         return self.title


# class Redaction(models.Model):
#     name = models.CharField(max_length=128)

#     def __str__(self):
#         return self.name

# from p_library.models import Author, Book
# from django.db.models import Count, F, Sum, ExpressionWrapper, DecimalField
# authors = Author.objects.all()
# annotated_authors = authors.annotate(books=Count("book_author"))
# authors_list = annotated_authors.filter(books__gt = 1)
# books = Book.objects.filter(author__in=authors_list)
# books_price = books.annotate(all_price=(ExpressionWrapper(F('price')*F('copy_count'), output_field=DecimalField())))
# books_sum = books_price.aggregate(Sum('all_price'))
# authors = Author.objects.filter(full_name="Douglas Adams")
# annotated_authors = authors.annotate(books=Count("book_author"))
# books = Book.objects.filter(author__in=annotated_authors)
# books_price = books.annotate(all_price=(ExpressionWrapper(F('price'), output_field=DecimalField())))
# books_sum = books_price.aggregate(Sum('all_price'))
