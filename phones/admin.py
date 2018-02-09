from django.contrib import admin

# Register your models here.

from phones.models import PhonePic,FinalPhone
from feedback.models import Feedback

admin.site.register(PhonePic)
admin.site.register(FinalPhone)
admin.site.register(Feedback)
