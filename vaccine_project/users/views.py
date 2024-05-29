from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm


def home(request):
    return render(request, 'base.html')

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    context = {
        'form': CreateUserForm()
    }
    return render(request, 'users/login.html')

def register(request):
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return redirect('register')

    form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
