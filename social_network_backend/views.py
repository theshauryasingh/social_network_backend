from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def signup(request):
    return 'signup called'

def signin(request):
    return 'signin called'