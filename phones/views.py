#--STANDARD LIBARIES--
#render sends to page with context
from django.shortcuts import render

#--CUSTOM CODE--
#import forms, models and custom functions
from .custom_functions import getRank
from .forms import InputForm
from .models import FinalPhone
#for json.dumps function
import json

# Create your views here.

def index(request):
	"""homepage view"""	
	#check if we've posted a search request
	if request.method != 'POST':
		#no data submitted, create a blank form
		form = InputForm()
	else:
		#search request submitted, first get a copy of the form
		form = InputForm(request.POST)
		
		if form.is_valid():
			#get input from form
			dataInput = form.clean()
			
			#get list of ranked phones
			rankedPhones = getRank(dataInput)
					
			#get ranked list of phones using cookies that store the inputs
			context = {'rankedPhones':rankedPhones,'rankedPhones_json':json.dumps(rankedPhones), 'form':form}

			#go to results page with the results sent via context
			return render(request,'phones/phone_results.html', context)

	context = {'form':form}

	#go to the homepage
	return render(request,'phones/index.html',context)

