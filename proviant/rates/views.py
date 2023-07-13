from django.shortcuts import redirect, render
from rates.forms import RatesForm


def form1_create(request):
    if request.method == 'POST':
        form = RatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')  # написать ссылку на html форму или узнать что вернуть
    else:
        form = RatesForm()
    return render(request, '', {'form': form})  # написать ссылку на html форму или узнать что вернуть
