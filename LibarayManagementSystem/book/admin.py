from django.contrib import admin
from .models import Book, Wishlist
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title','user','author','isbn','category']
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user','book_list']