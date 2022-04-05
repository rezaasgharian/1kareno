from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            User.objects.create_user(first_name=data['first_name'], last_name=data['last_name'],
                                     username=data['username'], email=data['email'], password=data['password1'])
            messages.success(request, 'You registered successfully!')
            return redirect('blog:login')
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


