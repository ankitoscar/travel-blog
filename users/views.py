from django.shortcuts import render, redirect
from django.contrib.auth import login 
from django.urls import reverse
from users.forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    return render(request, 'users/signup.html')

def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {"form": CustomUserCreationForm})
    elif request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("index"))

def logout(request):
    return render(request, 'users/logout.html')
