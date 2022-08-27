from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature, Doctor

# Create your views here.
def index(request):
    name = 'Tamir'
    return render(request, 'index.html', {'name': name})


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