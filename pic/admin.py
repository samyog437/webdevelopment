from django.contrib import admin

# Register your models here.
from .models import Pic, Review

admin.site.register(Pic)
admin.site.register(Review)