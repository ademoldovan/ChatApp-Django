from django.forms import ModelForm
from . import models


class CreateMessage(ModelForm):
    class Meta:
        model = models.Message
        fields = ['message']
