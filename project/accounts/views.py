from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from .models import Actor


def signup_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        actor_form = forms.CreateActor(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            actor = actor_form.save(commit=False)
            actor.user = user
            actor.isLoggedIn = True
            actor.save()
            # log the user in
            login(request, user)
            return redirect('chat:chat_view')
    else:
        user_form = UserCreationForm()
        actor_form = forms.CreateActor()
    return render(request, 'accounts/signup.html', {'user_form': user_form, 'actor_form': actor_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            current_actor = Actor.objects.get(user=user)
            current_actor.isLoggedIn = True
            current_actor.save()
            login(request, user)
            return redirect('chat:chat_view')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        current_user = request.user
        current_actor = Actor.objects.get(user=current_user)
        current_actor.isLoggedIn = False
        current_actor.save()
        logout(request)
        return redirect('homepage_view')
