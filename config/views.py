from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib import messages

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