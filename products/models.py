from django.db import models
from django.utils import timezone
from users.models import User, NULLABLE


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_data = models.DateField(default=timezone.now, verbose_name='Дата выхода продукта на рынок')
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.PROTECT, default=None)

    def __str__(self):
        return f'{self.name} {self.model} {self.release_data}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
