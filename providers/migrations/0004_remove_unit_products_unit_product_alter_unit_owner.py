# Generated by Django 5.0.2 on 2024-02-25 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('providers', '0003_remove_unit_contacts_remove_unit_products_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='products',
        ),
        migrations.AddField(
            model_name='unit',
            name='product',
            field=models.ManyToManyField(to='products.products', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='providers.unit', verbose_name='Поставщик'),
        ),
    ]