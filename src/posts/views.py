from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Post

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

        context = {
            'request': queryset
        }
        
    return render(request, 'search_results.html', context)

def get_cat_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))

    return queryset

def index(request):
    featured_posts = Post.objects.filter(featured=True)
    latest_posts = Post.objects.order_by('-timestamp')[0:3]

    context ={
        'featured_posts': featured_posts,
        'latest_posts': latest_posts,
    }
    
    return render(request, 'index.html', context)

def blog(request):
    post_list = Post.objects.all()
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    cat_count = get_cat_count()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'latest_posts': latest_posts,
        'cat_count': cat_count
    }

    return render(request, 'blog.html', context)

def post(request, id):
    return render(request, 'post.html', {})