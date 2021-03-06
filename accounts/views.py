from django.contrib import auth
from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import CreateUserForm, ForgotForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admins_only
from django_email_verification import sendConfirm

'''
my 3 wrappers -> @unauthenticated_user, @allowed_users, @admins_only
'''

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if(request.method == "POST"):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                sendConfirm(user)
                uname = user.username
                messages.success(request, "Please check you mail for account verification, " + uname +   " ! After that, you can successfully log-in !")
                return redirect('login')
            except:
                messages.info(request, "There is already an account with this email id! ")
                return redirect('signup')
        else:
            messages.info(request, "Please follow the guidelines for registering properly. ")
            form = CreateUserForm()
    

    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid username or Password")

    context = {}
    return render(request, 'accounts/login.html', context)

@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'products/home.html', context)

def logoutUser(request):
   if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
