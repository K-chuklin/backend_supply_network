from django.db import models
from django.utils import timezone


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_data = models.DateField(default=timezone.now, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        return f'{self.name} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
