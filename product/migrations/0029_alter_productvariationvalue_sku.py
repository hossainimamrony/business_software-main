# Generated by Django 4.1.2 on 2023-11-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_alter_addproduct_product_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariationvalue',
            name='sku',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
