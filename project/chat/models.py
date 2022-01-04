from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=300)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    message = models.CharField(max_length=300)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Image(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', null=False)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
