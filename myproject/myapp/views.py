from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = 'Tamir'
    return render(request, 'index.html', {'name': name})