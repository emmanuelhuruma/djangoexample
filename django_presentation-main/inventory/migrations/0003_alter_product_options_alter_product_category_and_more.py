# Generated by Django 5.1.4 on 2024-12-16 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_category_description_alter_product_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('change_stock', 'Can update stock quantity'), ('change_price', 'Can update product price')]},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
