from django.db import models
from django.utils import timezone
from products.models import Products


NULLABLE = {'blank': True, 'null': True}


class Unit(models.Model):
    CHAIN = [
        ('F', 'Завод'),
        ('R', 'Розничная сеть'),
        ('E', 'Индивидуальный предприниматель')
    ]
    name = models.CharField(max_length=100, verbose_name="Название компании")
    product = models.ManyToManyField(Products, verbose_name="Продукт")
    owner = models.ForeignKey('Unit', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)

    email = models.EmailField(max_length=30, verbose_name="Электронная почта", default=None)
    country = models.CharField(max_length=50, verbose_name="Страна", default=None)
    city = models.CharField(max_length=50, verbose_name="Город",  default=None)
    street = models.CharField(max_length=50, verbose_name="Улица",  default=None)
    house_number = models.CharField(max_length=50, verbose_name="Номер дома",  default=None)

    level = models.CharField(choices=CHAIN, verbose_name='Уровень цепи', default=None)
    debt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Задолженость", **NULLABLE)
    creations_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.owner} {self.name} {self.product} {self.level}'

    class Meta:
        verbose_name = 'Звено поставок'
        verbose_name_plural = 'Звенья поставок'
