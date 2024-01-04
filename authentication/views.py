from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm

# Create your views here.
def registration_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
        
    return render(request, 'register.html')


def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid username')
                return redirect('login')
            
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid password!')
            else:
                login(request, user)
                return redirect('index')

    return render(request, 'login.html', {"form": form})