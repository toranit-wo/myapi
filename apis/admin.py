from django.contrib import admin

# Register your models here.
from apis.models import Forehand,Backhand
admin.site.register(Forehand)
admin.site.register(Backhand)