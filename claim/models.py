from django.db import models

class Resource(models.Model):
	name = models.CharField(max_length=200)
	available = models.BooleanField(default=True)
	reservationTime = models.DateTimeField()
	reservationDuration = models.PositiveIntegerField(default=15)

	def __unicode__(self):
		return self.name
