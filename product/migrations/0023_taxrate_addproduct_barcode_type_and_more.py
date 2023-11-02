# Generated by Django 4.1.2 on 2023-11-01 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_addproduct_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax_name', models.CharField(max_length=255, unique=True)),
                ('tax_rate', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='addproduct',
            name='barcode_type',
            field=models.IntegerField(choices=[(1, 'Code 128'), (2, 'Code 39'), (3, 'EAN-13'), (4, 'EAN-8'), (5, 'UPC-A'), (6, 'UPC-E'), (7, 'ITF-14')], default=0),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='expires_in',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='expiry_period_unit',
            field=models.CharField(blank=True, choices=[('days', 'Days'), ('months', 'Months')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='addproduct',
            name='manage_stock',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0),
        ),
    ]
