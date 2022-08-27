from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature, Doctor

# Create your views here.
def index(request):
    name = 'Tamir'
    return render(request, 'index.html', {'name': name})


def main_page(request):
    feature_1 = Feature(1, 'Fast', 'This operates at light speed')
    feature_2 = Feature(2, 'Cheap', 'We do price matching')
    features = [feature_1, feature_2]
    doctor_1 = Doctor(1, 'Walter White', 'Chief Medical Officer', 'Not to be confused with the Breaking Bad guy')
    doctor_2 = Doctor(2, 'Handel Scholze Marques', 'Cardiology', 'Can bring back the dead')
    doctor_3 = Doctor(3, 'Tamir Einhorn Salem', "CEO's son", 'He does not work here')
    doctors = [doctor_1, doctor_2, doctor_3]
    return render(request, 'index.html', {'features': features, 'doctors': doctors})


def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split())
    context = {
        'number_of_words': number_of_words
    }
    return render(request, 'counter.html', context)