from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE())
    avatar = models.ImageField()

    def __str__(self):
        return self.name

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
