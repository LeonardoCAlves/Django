from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(request, username=username, password=senha)
        if user:
            login(request, user)
            return redirect('home')  # redireciona após login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'autenticacao/login.html')


from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def registrar(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registrar.html', {'form': form})
