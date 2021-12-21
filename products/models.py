from django.db import models
# Create your models here.
class Mahsulot(models.Model):
	name = models.TextField(max_length=200)
	image = models.ImageField(upload_to='images',blank = True)
	cost = models.IntegerField(blank = True)

	def __str__(self):
		return self.name