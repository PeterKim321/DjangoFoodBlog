from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Post, PostView, PostImage
from .forms import CommentForm

import folium

def contact(request):
    return render(request, 'contact.html')

def category_search(request):
    queryset = Post.objects.all()
    query = request.GET.get('query_name')
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    cat_count = get_cat_count()

    if query:
        queryset = queryset.filter(
            categories__title=query
        ).distinct()

    paginator = Paginator(queryset, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'request': paginated_queryset,
        'page_request_var': page_request_var,
        'query': query,
        'latest_posts': latest_posts,
        'cat_count': cat_count
    }
    
    return render(request, 'search_results.html', context)


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    cat_count = get_cat_count()

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()

    paginator = Paginator(queryset, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'request': paginated_queryset,
        'page_request_var': page_request_var,
        'query': query,
        'latest_posts': latest_posts,
        'cat_count': cat_count
    }

    return render(request, 'search_results.html', context)

def get_cat_count():
    queryset = Post.objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))

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
    post_list = Post.objects.all().order_by('-id')
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
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    latest_posts = Post.objects.order_by('-timestamp')[0:3]
    cat_count = get_cat_count()

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)
    
    
    form = CommentForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post_detail", kwargs = {
                'id': post.pk
            }))

    context ={
        'post': post,
        'photos': photos,
        'form': form,
        'latest_posts': latest_posts,
        'cat_count': cat_count
    }

    return render(request, 'post.html', context)
    
def map(request):
    loc_list = Post.objects.all().filter(announcement=False)
        
    m = folium.Map([-33.865143, 151.209900], zoom_start=12)

    for post in loc_list:
        url_redir = post.post_url()
        marker = folium.Html('<a href="{0}" target="_blank"> {1} - Score: {2}</a>'.format(url_redir, post.restaurant_name, post.getTotalScore()), script=True)
        popup = folium.Popup(marker, max_width=2650)
        folium.Marker(location=[post.latitude, post.longitude], popup=popup).add_to(m)
    
    m = m._repr_html_() #updated

    context = {
        "map" : m,
        "loc" : loc_list,
    }

    return render(request, 'map.html', context)

def ranking(request):
    # Sort by total score, in descending order
    post_list = sorted(Post.objects.all().filter(announcement=False), key=lambda x: x.getTotalScore(), reverse=True)
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

    return render(request, 'ranking.html', context)

