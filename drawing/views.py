from re import L
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def home(request):
    content = {}
    content['test'] = '5678392342'
    content['date'] = '2022/7/20'
    content['Bool'] = -2
    return render(request, 'home.html', content)
