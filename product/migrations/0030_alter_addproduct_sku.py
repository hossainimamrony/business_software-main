# Generated by Django 4.1.2 on 2023-11-01 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_alter_productvariationvalue_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='sku',
            field=models.CharField(max_length=36, unique=True),
        ),
    ]