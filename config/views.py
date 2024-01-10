from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm

from catalog.models import Movie, Show


class IndexView(View):
    def get(self, request):
        context = {}
        movies = Movie.objects.all()
        series = Show.objects.all()
        context["movies"] = movies
        context["series"] = series
        return render(request, 'index.html', context=context)


class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'config/login/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            next_page = request.GET.get('next', None)

            if next_page:
                return redirect(next_page)
            
            return redirect('index')
        else:
            messages.error(request, "Erro! Usuário ou senha incorreta")
            return redirect('login')



def logout_view(request):
    logout(request)
    
    return redirect('index')

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'config/register.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()

            next_page = request.GET.get('next', None)

            if next_page:
                return redirect(next_page)
            
            return redirect('index')
            # TO-DO: Criar página com mensagem de redirectionaento. return redirect('registration_success')

        else:
            messages.error(request, "Cadastro não realizado. Tente novamente")
            return redirect('register')