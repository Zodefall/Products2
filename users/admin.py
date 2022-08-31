from django.contrib import admin

# Register your models here.
from users.models import MyUserManager, User


admin.site.register(User)