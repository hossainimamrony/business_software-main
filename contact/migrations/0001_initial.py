# Generated by Django 4.2.6 on 2023-10-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Action', models.IntegerField(choices=[(0, 'Action'), (1, 'Pay'), (3, 'View'), (4, 'Edit'), (5, 'Delete')], default=0)),
                ('Contact_ID', models.CharField(max_length=1000, unique=True)),
                ('Business_Name', models.CharField(max_length=1000)),
                ('Name', models.CharField(max_length=1000)),
                ('Email', models.EmailField(max_length=1000, unique=True)),
                ('Address', models.CharField(max_length=1000)),
                ('Mobile', models.CharField(max_length=20, unique=True)),
                ('Tax_Number', models.TextField(unique=True)),
                ('Pay_Term', models.CharField(max_length=1000)),
                ('Total_Amount', models.TextField()),
                ('Advance_Amount', models.TextField()),
                ('Due_Amount', models.TextField()),
                ('Return_Due_Amount', models.TextField()),
                ('Paid_Status', models.CharField(choices=[(0, 'Checking'), (1, 'Payment Done'), (2, 'Due Running'), (3, 'Return Due Running')], default=0, max_length=100)),
            ],
        ),
    ]