from django.db import models


class Email(models.Model):
    email = models.EmailField(unique=True)


class Consultation(models.Model):
    CHOICES = [
        ('Детский сад/школа', 'Детский сад/школа'),
        ('Колледж/Университет', 'Колледж/Университет'),
        ('Комбинат питания', 'Комбинат питания'),
        ('Другое', 'Другое'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    choice = models.CharField(max_length=20, choices=CHOICES)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

