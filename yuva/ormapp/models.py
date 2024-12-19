from django.db import models
from django.contrib import admin
class Bank_loan(models.Model):
   Accno=models.IntegerField()
   name=models.CharField(max_length=100)
   phno=models.IntegerField()
   micr=models.IntegerField()
   ifsc=models.CharField(max_length=20)



class Bank_loanAdmin(admin.ModelAdmin):
   list_display=('Accno','name','phno','micr','ifsc')