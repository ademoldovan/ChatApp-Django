from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    message = models.CharField(max_length=300)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
