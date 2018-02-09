from django.db import models

class FinalPhone(models.Model):
	"""All the final data for a phone"""
	id_phone = models.CharField(max_length=20)
	#phone name, price, dimensions, release date and expert rating
	phone = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	dimension_x = models.DecimalField(max_digits=5, decimal_places=2)
	dimension_y = models.DecimalField(max_digits=5, decimal_places=2)
	dimension_z = models.DecimalField(max_digits=5, decimal_places=2)
	release_date = models.CharField(max_length=20)	
	market_rating = models.DecimalField(max_digits=2, decimal_places=1)
	
	#scores on main aspects
	photo_video = models.PositiveSmallIntegerField()
	play_media = models.PositiveSmallIntegerField()
	communicate = models.PositiveSmallIntegerField()
	gaming = models.PositiveSmallIntegerField()
	
	#link to purchase page
	#see https://stackoverflow.com/questions/417142/what-is-the-maximum-length-of-a-url-in-different-browsers
	link = models.CharField(max_length=2083)
	
	#features tags
	android = models.BooleanField()
	ios = models.BooleanField()
	dual_sim = models.BooleanField()	
	wd_resistant = models.BooleanField()
	fast_charge = models.BooleanField()	

class PhonePic(models.Model):
	"""stores the pictures for the phone"""
	phones = models.ForeignKey(FinalPhone,db_column='id_phone', null=True, blank=True, on_delete=models.SET_NULL)
	front_image = models.ImageField(upload_to="phones/phonepics")
	back_image = models.ImageField(upload_to="phones/phonepics")
