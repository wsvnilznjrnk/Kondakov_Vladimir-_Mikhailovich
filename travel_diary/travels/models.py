from django.db import models
from django.contrib.auth.models import User

class TravelEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)  # Местоположение
    image = models.ImageField(upload_to='travel_images/', blank=True, null=True)  # Изображение мест
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Стоимость путешествия
    convenience_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # Оценка удобства
    safety_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # Оценка безопасности
    population_density_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # Оценка населенности
    vegetation_rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], blank=True, null=True)  # Оценка растительности
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
