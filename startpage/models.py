from django.db import models
from django.contrib.auth.models import User
from django.core.cache import cache
import datetime
from kubik import settings


class Profile(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth = models.DateField(auto_now=True)
    photo = models.CharField(max_length=200, default='2.jpg')



class Chat(models.Model):
    type = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    invite_link = models.CharField(max_length=200)
    members = models.ManyToManyField(User, default=None)


class Message(models.Model):
    chat = models.ForeignKey(Chat, default=None, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=4096)
    is_read = models.BooleanField(default=False)

class UserChats(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, default=None, on_delete=models.CASCADE)