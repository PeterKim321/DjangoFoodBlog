from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import index, blog, post, search, category_search, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post_list'),
    path('post/<id>', post, name = 'post_detail'),
    path('search/', search, name = 'search'),
    path('category_search/', category_search, name = 'category_search'),
    path('contact/', contact, name='contact'),

    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', blog, name='post_list')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
