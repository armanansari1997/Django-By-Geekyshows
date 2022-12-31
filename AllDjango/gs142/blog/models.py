from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    desc = models.TextField(max_length=600)
    publish_date = models.DateTimeField()
