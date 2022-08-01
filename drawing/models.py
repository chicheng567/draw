
from django.db import models

# Create your models here.
class student(models.Model):
    gender_choices = [('F','female'), ('M','male')]
    area_choice = [('N', '北'), ('C', '中'), ('S', '南')]
    wish_choices = [('NM', '北弟'), ('NF', '北妹'), ('CM', '中弟'), ('CF', '中妹', ), ('SM', '南弟'), ('SF', '南妹')]

    id = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=10, null=False)
    gender = models.CharField(choices=gender_choices,max_length=1, default=0)
    yearNumber = models.IntegerField(default=0)
    family = models.IntegerField(null=True, default=None, blank=True)
    area = models.CharField(choices=area_choice, max_length=2,null=False, blank=False)
    high_school = models.CharField(max_length=20, default=None, blank=True)
    wish1 = models.CharField(choices=wish_choices,max_length=2, default=None, null=True, blank=True)
    wish2 = models.CharField(choices=wish_choices,max_length=2, default=None, null=True, blank=True)
    wish3 = models.CharField(choices=wish_choices,max_length=2, default=None, null=True, blank=True)


    def __str__(self):
        return f'{self.name}({self.id})'