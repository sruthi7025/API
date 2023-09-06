from django.shortcuts import render
import requests

def index(request):
    news=requests.get('https://saurav.tech/NewsAPI/top-headlines/category/health/in.json')
    posts = news.json()
    data = posts['articles']
    print(posts)
    return render(request,"index.html",{"posts":data})
