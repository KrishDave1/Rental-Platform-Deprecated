# Generated by Django 4.2.5 on 2023-10-01 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prime', '0004_remove_product_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='percent_Off',
            new_name='Percentage_off',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price_Was',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_Price',
            new_name='Price_was',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_ID',
            new_name='Product_Id',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_Image',
            new_name='Product_Image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='rating',
            new_name='Rating',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='reviews',
            new_name='Reviews',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='Type',
        ),
    ]
