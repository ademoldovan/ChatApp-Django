from django.forms import ModelForm, ImageField, CharField
from . import models


class CreateMessage(ModelForm):
    message = CharField(required=False)

    class Meta:
        model = models.Message
        fields = ['message']


class UploadImage(ModelForm):
    image = ImageField(required=False)

    class Meta:
        model = models.Image
        fields = ['image']
