from django.contrib import admin

# Register your models here.
from Market.models import Market, Category,UserProfile

admin.site.register(Market)
admin.site.register(Category)
admin.site.register(UserProfile)