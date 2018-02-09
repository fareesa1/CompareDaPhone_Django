#defines URL patterns for the phones app
from django.conf.urls import include,url
from . import views

#NEEDS TO BE INCLUDED IN ORDER TO REMEMBER APP/VIEW NAMESPACE
app_name='phones'

urlpatterns = [
	#homepage
    url(r'^$', views.index,name='index'),
]

