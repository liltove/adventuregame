from django.db import models

# Create your models here.
class PlayerChar(models.Model):
	NAME = models.CharField(max_length=128, unique=True)
	
	FEMALE = 'Female'
	MALE = 'Male'
	GENDER_CHOICES = (
		(FEMALE, 'Female'),
		(MALE, 'Male'),
	)
	GENDER = models.CharField(max_length=2,
								choices=GENDER_CHOICES,
								default=FEMALE)

	AGE = models.IntegerField(max_length=3,
								default=18)

	def ___unicode__(self):
		return self.name
