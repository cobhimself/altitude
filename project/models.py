from django.db import models

# Create your models here.
class Task(models.Model):
	name = models.CharField(max_length = 140)
	description = models.TextField()
	due_date = models.DateField()
	asignees = models.CommaSeparatedIntegerField(max_length = 100)
	dependancies = models.CommaSeparatedIntegerField(max_length = 100)

class Project(models.Model):
	name = models.CharField(max_length = 100)
	due_date = models.DateField()
	
