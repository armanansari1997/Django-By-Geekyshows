from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()

    # Change manager name from 'objects' to 'students'
    students = models.Manager()
