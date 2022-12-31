from django.db import models


# create table in Database
class User(models.Model):
    name = models.CharField(max_length=70, required=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
