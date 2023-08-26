from django.db import models
from accounts.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
     user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='users')
     title = models.CharField(max_length=120)
     book_image = models.ImageField(upload_to='images/',blank=True)
     author = models.CharField(max_length=50)
     isbn = models.PositiveIntegerField(primary_key=True)
     publication_date = models.DateTimeField(auto_now_add=True)
     category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='category')
     availability_status = models.BooleanField()
     stock = models.PositiveIntegerField()
     def __str__(self):
         return f'{self.isbn} - {self.title}'
     
class Wishlist(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    book = models.ManyToManyField(to=Book,related_name='books')
    def book_list (self):
        return ''.join([str(i) for i in self.book.all()])