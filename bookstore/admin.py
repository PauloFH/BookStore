from django.contrib import admin
from bookstore.models.author import Author

from bookstore.models.category import Category
from bookstore.models.publisher import Publisher
from bookstore.models.book import Book
from bookstore.models.purchase import Purchase
from bookstore.models.purchaseBooks import PurchaseBooks

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book)

class PurchaseBooksInline(admin.TabularInline):
    model = PurchaseBooks
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines =(PurchaseBooksInline,)