from django.contrib import admin
from .models import DetailsOfEvent,UserCreation,Attend
# Register your models here.
admin.site.register(DetailsOfEvent)
admin.site.register(UserCreation)
admin.site.register(Attend)