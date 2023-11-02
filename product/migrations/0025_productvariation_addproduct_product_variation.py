# Generated by Django 4.1.2 on 2023-11-01 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_variationtype_variationvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.variationtype')),
                ('variation_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.variationvalue')),
            ],
        ),
        migrations.AddField(
            model_name='addproduct',
            name='product_variation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productvariation'),
        ),
    ]