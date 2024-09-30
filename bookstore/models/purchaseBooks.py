from django.db import models
from .book import Book
from .purchase import Purchase
from django.contrib.auth.models import User

class PurchaseBooks(models.Model):
    purchase = models.ForeignKey(Purchase,
                                 on_delete=models.CASCADE,
                                 related_name='books')
    book = models.ForeignKey(Book,
                             on_delete=models.PROTECT,
                             related_name='+')
    quantity = models.IntegerField(default=1)
    class Meta:
        verbose_name_plural = 'puchases books'
    def __str__(self):
        return "{} ({})".format(self.book, self.purchase)