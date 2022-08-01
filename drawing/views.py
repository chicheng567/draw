from re import L
from django.shortcuts import render
from django.http import JsonResponse
from . import usedFunction
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    content = {}
    content['test'] = '5678392342'
    content['date'] = '2022/7/20'
    content['Bool'] = -2
    return render(request, 'home.html', content)

@csrf_exempt
def upload_file(request):
    content = {}
    if request.method == 'POST':
        file = request.FILES['data']
        usedFunction.handle_upload_file(file)
        usedFunction.handle_new_student(file.name)
        content['have_uploaded'] = 1
    return render(request, 'upload_file.html', content)


