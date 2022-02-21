from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        messages.success(request, 'You are already logged in')
        return render(request, 'pic/pics.html')
        

    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pic')
        else:
            messages.error(request, 'Please enter correct username or password')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    context = {'page':page, 'form':form} 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You registered an account')
            return redirect('login')
        else:
            messages.error(request, 'An error has occured')

    return render(request, 'users/login_register.html', context)

def profiles(request):
    return render(request, 'users/profiles.html')

def userProfile(request, pk):
    return render(request, 'users/user-profile.html')

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile

    pic = profile.pic_set.all()

    context={'profile':profile, 'pic':pic}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request, 'users/profile_form.html', context)


def adminManageAccount(request):
    if request.user.is_superuser:
        profile = Profile.objects.all()
    else:
        messages.error(request, "You don't have permission")
    context={'profile':profile}
    return render(request, 'users/adminManage.html', context)

def adminDeleteAccount(request, pk):
    if request.user.is_superuser:
        profile = Profile.objects.get(id=pk)
        profile.delete()
    else:
        messages.success(request, "You don't have permission")
    return render(request, 'users/adminManage.html')

    