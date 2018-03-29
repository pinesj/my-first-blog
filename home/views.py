from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def index2(request):
    msg = 'my Message'
    return render(request, 'index.html', {'message': msg})
