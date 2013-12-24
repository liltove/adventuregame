from django.db import models

# Create your models here.
class PlayerChar(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def ___unicode__(self):
		return self.name
