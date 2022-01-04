from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name