from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'Tamir'
    return render(request, 'index.html', {'name': name})


def counter(request):
    text = request.GET['text']
    number_of_words = len(text.split())
    context = {
        'number_of_words': number_of_words
    }
    return render(request, 'counter.html', context)