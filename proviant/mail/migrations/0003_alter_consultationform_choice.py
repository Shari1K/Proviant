# Generated by Django 4.2.2 on 2023-06-29 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_consultationform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultationform',
            name='choice',
            field=models.CharField(choices=[('Детский сад/школа', 'Детский сад/школа'), ('Колледж/Университет', 'Колледж/Университет'), ('Комбинат питания', 'Комбинат питания'), ('Другое', 'Другое')], max_length=20),
        ),
    ]
