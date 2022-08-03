from django.contrib import admin

from drawing.models import Family, student

# Register your models here.
admin.site.register(student)
admin.site.register(Family)