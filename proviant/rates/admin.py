from django.contrib import admin

from rates.models import Rate


@admin.register(Rate)
class RatesAdmin(admin.ModelAdmin):
    list_display = ()


#class RatesAdmin(admin.ModelAdmin):
#    list_display = ['Продукт', 'Тарифный план', 'Необходимое количество рабочих мест', 'Объем информационной базы',
#                    'Модуль кассовый учет', 'Значение', 'Рабочее место бухгалтера', 'Значение',
#                    'POS-моноблок + считыватель', 'Платежный терминал', 'Модуль транспортная карта',
#                    'Модуль вход/выход (СКУД)', 'Период', 'Имя', 'Почта', 'Номер телефона']
