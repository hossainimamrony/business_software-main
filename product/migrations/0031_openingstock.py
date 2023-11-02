# Generated by Django 4.1.2 on 2023-11-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0030_alter_addproduct_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=255, unique=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_cost_before_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lot_number', models.CharField(blank=True, max_length=255)),
                ('expiry_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]