from django.db import models

class Company(models.Model):

	company_name = models.CharField(max_length=50)
	company_location =models.CharField(max_length=50)



	def __str__(self):
		return self.company_name

