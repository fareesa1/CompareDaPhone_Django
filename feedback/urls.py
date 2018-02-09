"""Defines URL patterns for users"""
from django.conf.urls import url
from . import views

#NEEDS TO BE INCLUDED IN ORDER TO REMEMBER APP/VIEW NAMESPACE
app_name='feedback'

urlpatterns = [
	# Feedback form page
	url(r'^form_input/$', views.form_input, name='form_input'),
]
