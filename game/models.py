from django.db import models

# Create your models here.
class PlayerChar(models.Model):
	name = models.CharField(max_length=128)
	
	#FEMALE = 'Female'
	#MALE = 'Male'
	#GENDER_CHOICES = (
		#(FEMALE, 'Female'),
		#(MALE, 'Male'),
	#)
	#gender = models.CharField(max_length=2,
	#							choices=GENDER_CHOICES,
	#							default=FEMALE)

	age = models.IntegerField(default=18)

	def ___unicode__(self):
		return self.name

class ItemsOfWorld(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name