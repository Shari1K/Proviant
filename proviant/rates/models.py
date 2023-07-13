from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Rate(models.Model):
    Product = [
        ('Калькуляция', 'Калькуляция'),
        ('Безналичный расчет', 'Безналичный расчет'),
    ]
    Tariff = [
        ('Стандарт', 'Стандарт'),
        ('Оптиум', 'Оптиум'),
        ('Максимум', 'Максимум')
    ]
    Period = [
        ('1 мес.', '1 мес.'),
        ('3 мес.', '3 мес.'),
        ('6 мес.', '6 мес.'),
        ('12 мес.', '12 мес.')
    ]
    Product = models.CharField(max_length=20, choices=Product)
    Tariff = models.CharField(max_length=10, choices=Tariff, default=False)
    Number_of_workplaces = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(500)])
    Information_base_volume = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(1000)])
    Cashier_workplace = models.BooleanField(default=False)
    Cashier_quantity = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(50)])
    Accountant_workplace = models.BooleanField(default=False)
    Accountant_quantity = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(50)])
    Pos = models.BooleanField(default=False)
    Payment_terminal = models.BooleanField(default=False)
    Transport_Card = models.BooleanField(default=False)
    SKUD = models.BooleanField(default=False)
    Period = models.CharField(max_length=10, choices=Period, default=False)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=20)

