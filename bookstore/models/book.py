from django.db import models
from .author import Author
from .publisher import Publisher
from .category import Category

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbm = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ManyToManyField(Author,
                                    related_name='books')
    Category = models.ManyToManyField(Category,
                                      related_name='books')
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.PROTECT,
                                  related_name='books')
    def __str__(self):
        return "{}  ({})".format(self.name, self.publisher)
    class Meta:
        verbose_name_plural = 'books'
        