#this is where I store all custom functions for the phone ranking calculation

#import FinalPhone model for getRank function
from .models import FinalPhone, PhonePic
#this allows sorting of list of dictionaries
from operator import itemgetter
#allows use of complex lookups (filters) for models
from django.db.models import Q


def getRank(dataInput):
	""" suggests the top 5 phones based on user's input in form """
	#first obtain all inputs from the form
	price = dataInput.get("price")
	photo_video = dataInput.get("photo_video")
	play_media = dataInput.get("play_media")
	communicate = dataInput.get("communicate")
	gaming = dataInput.get("gaming")
	android = dataInput.get("android")
	ios = dataInput.get("ios")
	fast_charge = dataInput.get("fast_charge")
	dual_sim = dataInput.get("dual_sim")
	wd_resistant = dataInput.get("wd_resistant")
	released_2017 = dataInput.get("released_2017")
	
	#get list of phones that fall within budget
	resultPhones = FinalPhone.objects.filter(price__lte=price)
	
	#filter if any of the feature filters were selected
	if (android or ios):
		resultPhones = resultPhones.filter(Q(android=android) | Q(ios=ios))
	if (fast_charge):
		resultPhones = resultPhones.filter(fast_charge=True)
	if (dual_sim):
		resultPhones = resultPhones.filter(dual_sim=True)
	if (wd_resistant):
		resultPhones = resultPhones.filter(wd_resistant=True)
	if (released_2017):
		resultPhones = resultPhones.filter(release_date__contains="2017")
	
	#create list where you'll place phones, their names and final score
	scoredPhones = []
	
	#loop through each phone, calculate its score and add it to scoredPhones
	for phone in resultPhones:
		score = 0
		
		#add to score whichever is important
		if photo_video:
			score += phone.photo_video
		if play_media:
			score += phone.play_media
		if communicate:
			score += phone.communicate
		if gaming:
			score += phone.gaming
		
		#if none are important, add all of them
		if not(photo_video or play_media or communicate or gaming):
			score = phone.photo_video + phone.play_media + phone.communicate + phone.gaming
		
		#find PhonePic object related to phone
		imgurl = phone.phonepic_set.first().front_image.url
		
		#create a scoredPhone object that stores the existing phone features and its score
		#converted rating and price to string so that it can easily be sent to javascript
		scoredPhone = {"id":phone.id_phone,"name":phone.phone, "rating":str(phone.market_rating), 
			"price": str(phone.price), "score":score, "imgurl":imgurl, "photo_video":phone.photo_video,
			"play_media": phone.play_media, "communicate": phone.communicate, "gaming":phone.gaming, "link":phone.link}

		#add scoredPhone object to the results list
		scoredPhones.append(scoredPhone)	
	
	#sort phones by ranking in ascending order
	rankedPhones = sorted(scoredPhones, key=itemgetter("score","rating","price"))
	#return top 5 phones
	return rankedPhones[:5]
