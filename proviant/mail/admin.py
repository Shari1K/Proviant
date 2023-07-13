from django.contrib import admin
from .models import Email, Consultation


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Consultation)
class ConsultationformAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'choice', 'city', 'phone_number']
