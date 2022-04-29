from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .models import *


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(first_name=data['first_name'], last_name=data['last_name'],
                                     username=data['username'], email=data['email'], password=data['password1'])
            messages.success(request, 'You registered successfully!')
            Profile.objects.create(user= new_user)
            return redirect('account:login')
        else:
            errors = form.errors
            return render(request, 'account/register.html', {'form': form, 'errors': errors})
    else:
        form = RegisterForm()
        messages.error(request, 'You are not registered!')
        return render(request, 'account/register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('blog:index')
            else:
                return render(request, 'account/login.html', {'form': form})
        else:
            errors = form.errors
            print(errors)
            return render(request, 'account/login.html', {'form': form, 'errors': errors})
    return render(request, 'account/login.html')


def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("account:login")


def profile(request):
    user_profile = Profile.objects.get(user_id=request.user.id)
    profile_user = UserUpdateForm(request.POST, instance=request.user)
    profile_model = ProfileUpdateForm(request.POST, instance=request.user.profile)
    return render(request, 'account/profile.html', {'profile_user': profile_user, 'profile_model': profile_model, 'profile': user_profile})


def profileUpdate(request):
    if request.method == 'POST':
        profile_user = UserUpdateForm(data=request.POST, instance=request.user)
        profile_model = ProfileUpdateForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        if profile_user.is_valid() and profile_model.is_valid():
            profile_user.save()
            profile_model.save()
            return redirect('account:profile')
        # else:
        #     messages.error(request, 'error')
        #     return redirect("account:profile")
    else:
        profile_user = UserUpdateForm(instance=request.user)
        profile_model = ProfileUpdateForm(instance=request.user.profile)
    context = {'profile_user': profile_user, 'profile_model': profile_model}
    return render(request, 'account/profile.html', context)


def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
        else:
            print(form.errors)
            messages.error(request, 'Your password is not change successfully!')
            return redirect('account:profile')
    else:
        form = PasswordChangeForm(request.user, request.POST)
        return render(request, 'account/profile-update.html', {'form': form})
