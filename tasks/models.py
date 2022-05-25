from django.db import models

# Create your models here.

class Task(models.Model):
    task=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField()
    
