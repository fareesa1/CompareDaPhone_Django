from django.db import models

# Create your models here.
class Feedback(models.Model):
	"""all of the feedback data"""
	name = models.CharField(max_length=100)
	#email is optional
	email = models.EmailField(max_length=100,blank=True, default='')
	content = models.TextField()
	#add the date & time as a timestamp
	date_time = models.DateTimeField(auto_now_add=True)
	location = models.CharField(max_length=500)
