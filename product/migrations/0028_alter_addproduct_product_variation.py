# Generated by Django 4.1.2 on 2023-11-01 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0027_delete_taxrate_productvariation_applicable_tax_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='product_variation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariationvalue'),
        ),
    ]
