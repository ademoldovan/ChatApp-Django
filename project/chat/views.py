from django.forms import forms
from django.shortcuts import render, redirect
from .models import Message
from . import forms


def chat_view(request):
    messages = Message.objects.all().order_by('time')
    if request.method == 'POST':
        form = forms.CreateMessage(request.POST)
        if form.is_valid():
            # save article to database
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('chat:chat_view')
    else:
        form = forms.CreateMessage()
    return render(request, 'chat/chat.html', {'form': form, 'messages': messages})

