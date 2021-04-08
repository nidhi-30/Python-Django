from django.db import models

class PredResults(models.Model):
	mean_radius = models.FloatField()
	mean_texture = models.FloatField()
	mean_perimeter = models.FloatField()
	mean_area = models.FloatField()
	mean_smoothness = models.FloatField()
	classification = models.CharField(max_length=30)

	def __str__(self):
		return self.classification