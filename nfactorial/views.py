from django.shortcuts import render
from django.urls import include, path

# Create your views here.
def nfactorial(request):
    return path("", "Hello, nFactorial school!")
