import datetime
from django.utils import timezone
from django.db import models

SECONDS_PER_MINUTE = 60

class Resource(models.Model):
	name = models.CharField(max_length=200)
	available = models.BooleanField(default=True)
	reservationTime = models.DateTimeField()
	reservationDuration = models.PositiveIntegerField(default=15)

	def minutes_since_reservation(self):
		return (timezone.now() - self.reservationTime).seconds / SECONDS_PER_MINUTE

	def minutes_to_available(self):
		return (self.reservationTime + datetime.timedelta(minutes=self.reservationDuration) - timezone.now()).seconds / SECONDS_PER_MINUTE

	def __unicode__(self):
		return self.name
