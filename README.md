# Ex02 Django ORM Web Application
# Date:03-12-2024
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM:
![alt text](<Screenshot 2024-12-06 175028-1.png>)

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM:
```
models.py

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


admin.py

from django.contrib import admin
from .models import Bank_loan,Bank_loanAdmin
admin.site.register(Bank_loan,Bank_loanAdmin)

```
# OUTPUT:
![alt text](<Screenshot (38).png>)

![alt text](<Screenshot (39).png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
