from django.shortcuts import render
import requests

# Create your views here.
def p1(request):
    # data = requests.get('https://inshortsapi.vercel.app/news?category=all').json()["data"]
    return render(request, "p1.html", {"data" : []})

def base(request):
    data = requests.get('https://inshortsapi.vercel.app/news?category=all').json()["data"]
    return render(request, "base.html", {"data" : data})
    
def home(request):
    data = requests.get('https://inshortsapi.vercel.app/news?category=all').json()["data"]
    return render(request, "home.html", {"data" : data})

def business(request):
    data = requests.get('https://inshortsapi.vercel.app/news?category=business').json()["data"]
    return render(request, "business.html", {"data" : data})
    
def entertainment(request):
    data = requests.get('https://inshortsapi.vercel.app/news?category=entertainment').json()["data"]
    return render(request, "entertainment.html", {"data" : data})

def sports(request):
    data = requests.get('https://inshortsapi.vercel.app/news?category=sports').json()["data"]
    return render(request, "sports.html", {"data" : data})