from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from . import models


class CreateActor(ModelForm):
    class Meta:
        model = models.Actor
        fields = ('email',)
