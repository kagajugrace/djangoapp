from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Employees(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.firstname

class Album(models.Model): 
	title = models.CharField(max_length = 30) 
	artist = models.CharField(max_length = 30) 
	genre = models.CharField(max_length = 30) 

	def __str__(self): 
		return self.title 

class Song(models.Model): 
	name = models.CharField(max_length = 100) 
	album = models.ForeignKey(Album, on_delete = models.CASCADE) 

	def __str__(self): 
		return self.name 
    
class Registration(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    def __str__(self):
        return self.firstname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    country =models.CharField(max_length=255)
    accounttype =models.CharField(max_length=255)
    gender =models.CharField(max_length=255)


## serializers.py - Tele
## create a profile serializers
