# Generated by Django 4.1.2 on 2023-10-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_addproduct_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warranty',
            name='warranty_duration_type',
            field=models.IntegerField(choices=[(0, 'Days'), (1, 'Months'), (2, 'Years')], default=0, max_length=1000),
        ),
    ]