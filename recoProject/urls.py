"""recoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#modules that manage URLs for the project and admin site
from django.conf.urls import include, url
from django.contrib import admin
#added to enable link to images in media folder which stores product images: https://stackoverflow.com/a/37967034
from django.conf.urls.static import static
from django.conf import settings


#directs user to the right page
urlpatterns = [
	#to admin page
    url(r'^admin/', admin.site.urls),
    #to url list for phones app
    url(r'', include('phones.urls')),
    #to url list for feedback app
    url(r'^feedback/',include('feedback.urls')),
#added in the end link to media folder, see above reference
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
