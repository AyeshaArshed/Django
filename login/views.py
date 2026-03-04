from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .form import LoginForm, SignupForm

User = get_user_model()

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            phone_no = form.cleaned_data.get('phone_no') or None
            user = User.objects.create_user(
                username=username,
                password=password,
                phone_no=phone_no
            )
            messages.success(request, "Account created successfully!")
            return redirect('login')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('list_book')
    form = LoginForm(request.POST or None)
    username_prefill = ''
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request, user)
                return redirect(request.GET.get('next') or 'list_book')
            else:
                messages.error(request, "Invalid username or password")
                username_prefill = username
        else:
            messages.error(request, "Please fill in both username and password")

    form.fields['username'].initial = username_prefill
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')