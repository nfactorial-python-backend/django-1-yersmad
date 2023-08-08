from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("<int:first>/add/<int:second>/", views.add, name="add func"),
    path("transform/<str:text>/", views.upper, name="transform to upper"),
    path("check/<str:word>/", views.ispalindrome, name="check palindrome text"),
    path("calc/<int:first>/<str:operation>/<int:second>/", views.calc, name="calculator"),
    path("randomnumber/<int:min>/<int:max>/", views.random_number, name="randomizer"),
    path("reverse/<str:text>/", views.reverse, name="reverse text"),
    path("factorial/<int:number>/", views.factorial, name="factorial of number"),
]
