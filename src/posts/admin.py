from django.contrib import admin

from .models import Author, Category, Post, Comment, models, PostView, PostImage
from tinymce.widgets import TinyMCE

class PostImageAdmin(admin.StackedInline):
    model = PostImage

class TinyMCEAdmin(admin.ModelAdmin):
    formfield_overides ={
        models.TextField: { 'widget': TinyMCE() }
    }
    
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(PostView)
admin.site.register(Post, TinyMCEAdmin)
admin.site.register(PostImage)
