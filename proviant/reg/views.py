from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')  # написать ссылку на html форму или узнать что вернуть
    else:
        form = RegistrationForm()
    return render(request, '...', {'form': form})   # написать ссылку на html форму или узнать что вернуть


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return redirect('') # написать ссылку на html форму или узнать что вернуть
            else:
                messages.error(request, 'Неправильный пароль.')
        except UserProfile.DoesNotExist:
            messages.error(request, 'Неправильный логин.')

        return render(request, '')  # написать ссылку на html форму или узнать что вернуть
    else:
        return render(request, '')  # написать ссылку на html форму или узнать что вернуть
