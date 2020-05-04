from django.db import models

# Create your models here.


class User(models.Model):
    firs_name = models.CharField(max_length=264, unique=True)
    last_name = models.CharField(max_length=264, unique=True)
    email = models.EmailField(max_length=264, unique=True)
