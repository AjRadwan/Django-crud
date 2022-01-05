from django.db import models
 
# Create your models here.

 
class Student(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200,  blank=False)
    address = models.CharField(max_length=200,  blank=False)
 
    def __str__(self):
        return self.name