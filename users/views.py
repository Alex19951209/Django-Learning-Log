from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Показати порожню форму руєстрації.
        form = UserCreationForm()
    else:
        # Опрацювати заповнену форму.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Авторизувати користувача та скерувати  його на головну сторінку.
            login(request, new_user)
            return redirect('learning_logs:index')
    # Показати порожню або недійсну форму.
    context = {'form': form}
    return render(request, 'registration/register.html', context)



def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logget out. Thank you for visiting!"))
    return redirect('learning_logs:index')