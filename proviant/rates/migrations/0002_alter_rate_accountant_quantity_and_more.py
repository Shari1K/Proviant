# Generated by Django 4.2.2 on 2023-07-02 14:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='Accountant_quantity',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Cashier_quantity',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)]),
        ),
        migrations.AlterField(
            model_name='rate',
            name='Period',
            field=models.CharField(choices=[('1 мес.', '1 мес.'), ('3 мес.', '3 мес.'), ('6 мес.', '6 мес.'), ('12 мес.', '12 мес.')], default=False, max_length=10),
        ),
    ]