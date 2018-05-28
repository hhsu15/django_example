from django.db import models
# ORMr
# Essentially you define the database tables here
# Create your models here.
class Airport(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length=64)

	def __str__(self):
		return f"id: {self.id} - {self.city} - {self.code}"

class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
	destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
	duration = models.IntegerField()

	def __str__(self):
		return "id: {} - From {} to {}. Duration:{}".format(self.id, self.origin, self.destination, self.duration)