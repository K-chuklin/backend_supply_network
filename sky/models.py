from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Contacts(models.Model):
    email = models.EmailField(max_length=30, verbose_name="Электронная почта")
    country = models.CharField(max_length=50, verbose_name="Страна")
    city = models.CharField(max_length=50, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.IntegerField(verbose_name="Номер дома")

    def __str__(self):
        return f'{self.email}{self.country}{self.city}'

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    release_data = models.DateField(verbose_name='Дата выхода продукта на рынок', **NULLABLE)

    def __str__(self):
        return f'{self.name}{self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Unit(models.Model):
    CHAIN = [
        ('F', 'Завод'),
        ('R', 'Розничная сеть'),
        ('E', 'Индивидуальный предприниматель')
    ]
    name = models.CharField(max_length=100, verbose_name="Название")
    contacts = models.ForeignKey(Contacts, default=None,
                                 on_delete=models.CASCADE, verbose_name="Контакты")
    products = models.ForeignKey(Products, default=None,
                                 on_delete=models.CASCADE, verbose_name="Проукдты")
    shipper = models.CharField(choices=CHAIN, verbose_name='поставщик')
    arrears = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Задолженость")
    creations_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.name}{self.contacts}{self.arrears}'

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'
