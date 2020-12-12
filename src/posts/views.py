from django.shortcuts import render
from .models import Post

def index(request):
    featured_posts = Post.objects.filter(featured=True)
    latest_posts = Post.objects.order_by('-timestamp')[0:3]

    context ={
        'featured_posts': featured_posts,
        'latest_posts': latest_posts,
    }
    
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html', {})

def post(request):
    return render(request, 'post.html', {})