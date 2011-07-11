from django.db import models
from django.contrib.auth.models import User
from altitude.accounts import Department

# Create your models here.

class Project(models.Model):
	name = models.CharField(max_length = 100)
    acronym = models.CharField(max_length = 5)
	due_date = models.DateField()
	
class Milestone(models.Model):
    name = models.CharField(max_length = 140)
    description = models.TextField()
    due_date = models.DateField()
    project = models.ForeignKey('Project')

class Element(models.Model):
    name = models.CharField(max_length = 140)
    project = models.ForeignKey('Project')
    order = models.IntegerField()
    percentComplete = models.DecimalField(max_digits=5, decimal_places=2)

class DepartmentTask(models.Model):
    parentElement = models.ForeignKey(Element)
    department = models.ForeignKey(Department)

class Task(models.Model):
	name = models.CharField(max_length = 140)
    project = models.ForeignKey('Project')
	description = models.TextField()
	due_date = models.DateField()
	asignees = models.ManyToManyField(User)
	dependancies = models.ManyToManyField('self')

