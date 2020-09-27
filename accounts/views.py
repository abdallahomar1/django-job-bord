from django.shortcuts import render
from .forms import SingupForm
from django.contrib.auth import authenticate, login
from .models import Profile
# Create your views here.
def signup(request):
    if request.method=="POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login = (request,user)
            
            
    else:
        form = SingupForm()  

    return render(request, 'registration/sinup.html', {'form':form})


def profile(request):
    profile = Profile.objects.get(user= request.user)
    return render(request, 'accounts/profile.html', {'profile':Profile})


def profileedite(request):
    pass