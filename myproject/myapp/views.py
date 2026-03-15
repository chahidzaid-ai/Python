from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Feature


def index(request):
    features = Feature.objects.all()
    context = {
        'name': 'Zaid',
        'age': 21,
        'features': features,
    }
    return render(request, 'index.html', context)


def counter(request):
    if request.method == 'POST':
        text = request.POST['text']
    else:
        text = request.GET.get('text', '')
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email existe déjà')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username existe déjà')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Mots de passe non identiques')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalides')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')