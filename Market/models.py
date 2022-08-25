from django.contrib.auth.models import User
from django.db import models
from gdstorage.storage import GoogleDriveStorage

gd_storage = GoogleDriveStorage()

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    avatar = models.ImageField(upload_to='photos',default='default.png',blank=True,storage=gd_storage)

    def __str__(self):
        return self.user.username

class Market(models.Model):
    name = models.CharField(max_length=40)
    price = models.IntegerField()
    weight = models.CharField(max_length=20)
    category = models.ForeignKey('category', on_delete=models.PROTECT)


    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
