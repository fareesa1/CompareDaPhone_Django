#this is where we store our forms - testing

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
	"""feedback form"""
	class Meta:
		model = Feedback
		fields = ['name','email','content','location']
		labels = {'name': 'Name', 'email': "Email", 'content':"Feedback", 'location':''}
		widgets = {'content': forms.Textarea(attrs={'rows':3}),'location': forms.TextInput(attrs={'type':'hidden'})}
