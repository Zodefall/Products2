from django import forms
from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from Market.models import Market, Category


#
# class NewsAdminForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = '__all__'





admin.site.register(Market)
admin.site.register(Category)
