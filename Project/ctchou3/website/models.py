from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length = 50)
    instructor = models.CharField(max_length = 50)
    location = models.CharField(max_length = 100)
    time = models.CharField(max_length = 100)
    final = models.CharField(max_length = 100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name