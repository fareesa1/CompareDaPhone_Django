#this is where we store our forms

from django import forms

class InputForm(forms.Form):
	"""form that contains all of our questionnaire inputs"""

	#budget input
	price = forms.DecimalField(max_digits=6, decimal_places=2)
	
	#preferences input
	photo_video = forms.BooleanField(required=False, initial=False)
	play_media = forms.BooleanField(required=False, initial=False)
	communicate = forms.BooleanField(required=False, initial=False)
	gaming = forms.BooleanField(required=False, initial=False)
	
	#features filter input
	android = forms.BooleanField(required=False, initial=False)
	ios = forms.BooleanField(required=False, initial=False)
	fast_charge = forms.BooleanField(required=False, initial=False)
	dual_sim = forms.BooleanField(required=False, initial=False)	
	wd_resistant = forms.BooleanField(required=False, initial=False)	
	released_2017 = forms.BooleanField(required=False, initial=False)	
