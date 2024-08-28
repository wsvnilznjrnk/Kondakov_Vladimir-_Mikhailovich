from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Rental(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    rental_period = models.CharField(max_length=20, choices=[('2 недели', '2 недели'), ('месяц', 'месяц'), ('3 месяца', '3 месяца')])
    return_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.return_date:
            if self.rental_period == '2 недели':
                self.return_date = self.rental_date + timedelta(weeks=2)
            elif self.rental_period == 'месяц':
                self.return_date = self.rental_date + timedelta(weeks=4)
            elif self.rental_period == '3 месяца':
                self.return_date = self.rental_date + timedelta(weeks=12)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'
