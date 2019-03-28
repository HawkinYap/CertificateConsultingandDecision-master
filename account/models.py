from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    stunamber = models.CharField(max_length=20, null=True)
    major = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User, unique=True)
    school = models.CharField(max_length=100, blank=True)
    major = models.CharField(max_length=100, blank=True)
    getcert = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100 , blank=True)
    aboutme = models.TextField(blank=True)
    img = models.ImageField(upload_to='img' , blank=True)

    def __str__(self):
        return 'user:{}'.format(self.user.username)


class File(models.Model):
    file = models.FileField(upload_to='file')
    name = models.CharField(max_length=20)