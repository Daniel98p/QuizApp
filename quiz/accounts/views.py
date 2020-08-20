from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'accounts/home.html')


def signup(request):
    form = CustomUserCreationForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'accounts/signup.html', {'form': form})
