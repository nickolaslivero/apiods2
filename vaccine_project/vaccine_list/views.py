from django.shortcuts import render, redirect

import requests
import random 
from uuid import uuid4

def home(request):
    user = request.user
    if not user or not user.is_authenticated:
        return redirect('login')

    response = requests.get(f'http://127.0.0.1:8000/blocks/{request.user.username}')
    context = {
        'vaccine_list': response.json()
    }

    return render(request, 'vaccine_list/vaccine_list.html', context)


def add_vaccine(request):
    user = request.user
    if not user or not user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        vaccine_name = request.POST.get('vaccine_name')
        date = request.POST.get('date')

        data = dict(
            id=str(uuid4()),
            username=request.user.username,
            vaccine_name=vaccine_name,
            date=date,
        )

        requests.post('http://127.0.0.1:8000/blocks', json=data)

        return redirect('home')

    return render(request, 'vaccine_list/add_vaccine.html')
