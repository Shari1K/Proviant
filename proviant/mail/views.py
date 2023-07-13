from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ConsultationForm
from .models import Email


def save_email(request):
    email = request.POST.get('email')
    if email:
        Email.objects.create(email=email)
        return HttpResponse('Email сохранен!')
    else:
        return HttpResponse('Email неправильный')


def save_consultationform(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = ConsultationForm()
    return render(request, '', {'form': form})  # написать ссылку на html форму или узнать что вернуть
