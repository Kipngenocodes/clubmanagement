from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def login_student(request):
    pass


def logout_student(request):
    pass
