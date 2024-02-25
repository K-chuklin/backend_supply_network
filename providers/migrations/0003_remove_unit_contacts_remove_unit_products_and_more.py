# Generated by Django 5.0.2 on 2024-02-25 17:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('providers', '0002_alter_contacts_options_alter_products_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='products',
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name': 'Звено поставок', 'verbose_name_plural': 'Звенья поставок'},
        ),
        migrations.RemoveField(
            model_name='unit',
            name='arrears',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='shipper',
        ),
        migrations.AddField(
            model_name='unit',
            name='city',
            field=models.CharField(default=None, max_length=50, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='unit',
            name='country',
            field=models.CharField(default=None, max_length=50, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='unit',
            name='debt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Задолженость'),
        ),
        migrations.AddField(
            model_name='unit',
            name='email',
            field=models.EmailField(default=None, max_length=30, verbose_name='Электронная почта'),
        ),
        migrations.AddField(
            model_name='unit',
            name='house_number',
            field=models.CharField(default=None, max_length=50, verbose_name='Номер дома'),
        ),
        migrations.AddField(
            model_name='unit',
            name='level',
            field=models.CharField(choices=[('F', 'Завод'), ('R', 'Розничная сеть'), ('E', 'Индивидуальный предприниматель')], default=None, verbose_name='Уровень цепи'),
        ),
        migrations.AddField(
            model_name='unit',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор продукта'),
        ),
        migrations.AddField(
            model_name='unit',
            name='street',
            field=models.CharField(default=None, max_length=50, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='creations_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название компании'),
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.AddField(
            model_name='unit',
            name='products',
            field=models.ManyToManyField(to='products.products', verbose_name='Проукдты'),
        ),
    ]