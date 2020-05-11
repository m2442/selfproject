from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def page1(request):
    name = request.GET['name']
    age = request.GET['age']
    college = request.GET['college']
    city = request.GET['city']
    # dict = {}
    # dict['name'] = name
    # dict['age'] = age
    # dict['college'] = college
    # dict['city'] = city
    return render(request, 'page1.html', {'name': name, 'age': age, 'college': college, 'city': city})


def page2(request):
    return render(request, 'page2.html')

def about(request):
    return render(request, 'about.html')
