from django.db import models

class Resource(models.Model):
	name = models.CharField(max_length=200)
	available = models.BooleanField()
