from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()