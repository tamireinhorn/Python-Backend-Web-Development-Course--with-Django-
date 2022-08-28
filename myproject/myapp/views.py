from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature, Doctor
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def index(request):
    name = 'Tamir'
    return render(request, 'index.html', {'name': name})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already in use')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already in use')
                return redirect('register')
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            return redirect('login')
        else:
            messages.info(request, "Passwords inputted were not the same")
    return render(request, 'register.html')


def main_page(request):
    features = Feature.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'index.html', {'features': features, 'doctors': doctors })


def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split())
    context = {
        'number_of_words': number_of_words
    }
    return render(request, 'counter.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk: str):
    return render(request, 'post.html', {'pk': pk})


def hub(request):
    posts = [1, 2, 3, 'zap', 'muito zap', 4, 5]
    return render(request, 'hub.html', {'posts': posts})