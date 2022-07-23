from django.contrib import admin

# Register your models here.
from Market.models import Market, Category

admin.site.register(Market)
admin.site.register(Category)