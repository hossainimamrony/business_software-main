# Generated by Django 4.1.2 on 2023-10-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0020_alter_addproduct_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='sku',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]