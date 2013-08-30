from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=200)
	image = models.URLField()
	price = models.IntegerField()
	description = models.TextField()