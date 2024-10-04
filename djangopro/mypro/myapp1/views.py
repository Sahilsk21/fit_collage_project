from django.shortcuts import render

from django.shortcuts import render, redirect
from .froms import UserInfoForm
from .models import UserInfo 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, LoginForm

def user_info_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_info_display')
    else:
        form = UserInfoForm()

    return render(request, 'myapp/user_info_form.html', {'form': form})

def user_info_display(request):
    user_info = UserInfo.objects.all()
    return render(request, 'myapp/user_info_display.html', {'user_info': user_info}) 


##loging part code 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'myapp/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')