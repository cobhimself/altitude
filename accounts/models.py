from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	departments = models.CommaSeparatedIntegerField(max_length = 100)
	def __str__(self):
		return self.user;

class Department(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name;
