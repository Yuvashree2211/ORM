
from django.db import models
from django.contrib import admin
class Bankloan (models.Model):
    Accno=models.IntegerField()
    name=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=20)
    micr=models.IntegerField()
    phno=models.IntegerField()

 
class BankloanAdmin(admin.ModelAdmin):
    list_display=('Accno','name','ifsc','micr','phno')