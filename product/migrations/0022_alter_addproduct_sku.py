# Generated by Django 4.1.2 on 2023-10-29 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0021_alter_addproduct_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='sku',
            field=models.CharField(editable=False, max_length=36, unique=True),
        ),
    ]
