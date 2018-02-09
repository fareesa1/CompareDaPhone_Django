#--STANDARD LIBARIES--
#render sends to page with context and HttpResponseRedirect to send without context
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
def form_input(request):
	"""processes form input"""
	#if got to the page via get, you create new form
	#if through post, you use the post data from the form
	if request.method != "POST":
		form = FeedbackForm()
	else:	
		form = FeedbackForm(request.POST)
		#if form input is valid, temporarily save it in database
		if form.is_valid():
			form.save()
			return render(request, "feedback/feedback_success.html")
			
	context = {'form': form}
	return render(request,'feedback/feedback_form.html', context)
