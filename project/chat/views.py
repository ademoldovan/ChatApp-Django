from django.shortcuts import render, redirect
from . import forms
from .models import Message, Image
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/ ")
def chat_view(request):
    messages = Message.objects.all().order_by('time')
    images = Image.objects.all().order_by('time')
    i = 0
    j = 0
    n = len(messages)
    m = len(images)
    elements = []
    while i < n and j < m:
        if messages[i].time < images[j].time:
            elements.append(messages[i])
            i = i + 1
        else:
            elements.append(images[j])
            j = j + 1
    if i < n:
        while i < n:
            elements.append(messages[i])
            i = i + 1
    if j < m:
        while j < m:
            elements.append(images[j])
            j = j + 1
    if request.method == 'POST':
        form = forms.CreateMessage(request.POST)
        image_form = forms.UploadImage(request.POST, request.FILES)
        if form.is_valid():
            # save article to database
            instance = form.save(commit=False)
            if instance.message:
                instance.user = request.user
                instance.save()
        if image_form.is_valid():
            image_instance = image_form.save(commit=False)
            if image_instance.image:
                image_instance.user = request.user
                image_instance.name = request.user.username
                image_instance.save()
                return redirect('chat:chat_view')
        return redirect('chat:chat_view')
    else:
        form = forms.CreateMessage()
        image_form = forms.UploadImage()
    return render(request, 'chat/chat.html', {'form': form, 'image_form': image_form, 'messages': messages,
                                              'images': images, 'elements': elements})
