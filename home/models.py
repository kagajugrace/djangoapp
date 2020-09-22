from django.db import models

# Create your models here.
class Employees(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.firstname