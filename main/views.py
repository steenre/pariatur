from django.shortcuts import render
from blogger.models import Post, Category
import os, requests
from django.core.paginator import Paginator
from django.utils.text import slugify
from dotenv import load_dotenv
load_dotenv()

def index(request):
    return render(request, 'main/index.html')

def posts(request):
    url = "https://newsapi.org/v2/everything"
    api_key = os.environ.get('apiKey')
    posts = requests.get(url, params={
        'q':request.GET.get('q', 'music'),
        'apiKey': api_key
    }).json()
    
    articles = posts.get('articles', [])
    for article in articles:
            article['slug'] = slugify(article['title'])
    
    context = {
        'posts':articles
    }
    return render(request, 'main/posts.html', context)

def post(request, slug):
    url = "https://newsapi.org/v2/everything"
    api_key = os.environ.get('apiKey')
    post = requests.get(url, params={
        'q': slug,
        'apiKey': api_key
    }).json().get('articles')[0]
    context = {
        'post':post
    }
    return render(request, 'main/post.html', context)
    