from django.db import models

# Create your models here.

class Form(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)

    def __str__(self):
        return self.name