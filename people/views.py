from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.

def register(request, template='user/register.html'):
    if request.user.is_authenticated():
        return redirect('index')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
            )
            new_user.set_password(form.cleaned_data["password"])
            new_user.name = form.cleaned_data["name"]
            new_user.blood_type = form.cleaned_data["blood_type"]
            new_user.phone = form.cleaned_data["phone"]
            new_user.is_active = True
            new_user.save()
            success = "<h1> Successfully registered!"
            return HttpResponse(success)
    else:
        form = RegisterForm()
    return render(request, template, {'form': form})

def user_login(request, template='user/login.html'):
    if request.user.is_authenticated():
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        blood_type = request.POST['blood_type']
        user = authenticate(username=username, password=password, blood_type=blood_type)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('account inactive')
        else:
            return HttpResponse('username/password/blood type incorrect')
    else:
        pass
    form = LoginForm()
    return render(request, template, {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')
