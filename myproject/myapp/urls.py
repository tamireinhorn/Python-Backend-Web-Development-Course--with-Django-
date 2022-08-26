from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    # The first argument is the actual route in the site, the url. The second will get the function to return and the last is the name of the page.
    path('counter', views.counter, name = 'counter')
]