from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import *
from .models import *


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in.'
                return HttpResponseRedirect(reverse('crm'))
            else:
                message = 'Login failed'
    return render(request, 'login.html', {'form': form, 'message': message})



@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'crm.html', {'tasks': tasks})