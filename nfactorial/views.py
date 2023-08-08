from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import BadRequest


# Create your views here.
def hello(request):
    return HttpResponse("Hello, nFactorial school!")

def add(request, first, second):
    result = first+second
    return HttpResponse(f"{first}+{second}={result}")

def upper(request, text):
    return HttpResponse(text.upper())

def ispalindrome(request, word):
    return HttpResponse(word == word[::-1])

def calc(request, first, operation, second):
    if operation == "add":
        return HttpResponse(f"{first}+{second}={first+second}")

    elif operation == "sub":
        return HttpResponse(f"{first}-{second}={first-second}")

    elif operation == "mult":
        return HttpResponse(f"{first}*{second}={first*second}")

    elif operation == "div":
        return HttpResponse(f"{first}:{second}={first//second}")

    else:
        raise BadRequest("Invalid parametres")
