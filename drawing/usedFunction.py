from django.http import HttpResponseRedirect
from django.shortcuts import render
import openpyxl
from .models import *
from django.db import connection
county = {('臺北市', '新北市', '基隆市', '新竹市', '桃園市', '新竹縣', '宜蘭縣', '台北市') : 'N',
('臺中市', '苗栗縣', '彰化縣', '南投縣', '雲林縣') : 'C',
('高雄市', '臺南市', '嘉義市', '嘉義縣', '屏東縣', '澎湖縣'): 'S',}

county_map = {}
for k, v in county.items():
    for key in k:
        county_map[key] = v

def handle_upload_file(f):
    location = 'uploadFile/' + f.name
    with open(location, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def handle_new_student(fileName):
    file = openpyxl.load_workbook('uploadFile/' + fileName)
    sheet = file.active
    iter = 0
    grade = int(fileName[:3])
    for row in sheet:
        if iter > 0:
            if row[0].value == None:
                break
            Id = row[1].value
            Name = row[2].value
            gender = row[3].value
            city = row[10].value[0:3]
            High_school = row[13].value
            if student.objects.filter(id=Id).count() < 1:
                new_student = student(id=Id, name = Name, area = county_map[city], high_school = High_school)
                if gender == 2:
                    new_student.gender = 'F'
                else:
                    new_student.gender = 'M'
                
                new_student.yearNumber = grade
                new_student.save()
                
        iter += 1