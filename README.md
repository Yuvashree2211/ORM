# Ex02 Django ORM Web Application
# Date:03-12-2024
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM:
![Screenshot 2024-12-06 175028](https://github.com/user-attachments/assets/41a357a3-c7c6-403b-bbe2-86b33e1be2b1)

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
class Bankloan (models.Model):
    Accno=models.IntegerField()
    name=models.CharField(max_length=100)
    ifsc=models.CharField(max_length=20)
    micr=models.IntegerField()
    phno=models.IntegerField()

 
class BankloanAdmin(admin.ModelAdmin):
    list_display=('Accno','name','ifsc','micr','phno')

admin.py

from django.contrib import admin
from .models import Bankloan,BankloanAdmin
admin.site.register(Bankloan,BankloanAdmin)

```
# OUTPUT:
![alt text](<Screenshot (14).png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
