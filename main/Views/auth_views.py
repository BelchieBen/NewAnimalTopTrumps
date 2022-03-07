from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, FormView
from ..forms.auth_forms import registerForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

class register(View):
    def get(self, request, *args, **kwargs):
        form = registerForm()
        return render(request, 'main/auth/register.html', context={"register_form":form})

    def post(self, request, *args, **kwargs):
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successfull")
            return redirect('home')
        messages.error(request, "Registration Unsuccessful")
        return redirect('register')

class Login(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, 'main/auth/login.html', context={"login_form":form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,'Authentication successful, you are now logged in {username}.')
                return redirect('home')
            else:
                messages.error('Authentication failed')

def Logout(request):
    logout(request)
    return redirect('login')
