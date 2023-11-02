# Generated by Django 4.1.2 on 2023-10-28 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_brand_category_alter_addproduct_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.brand'),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]