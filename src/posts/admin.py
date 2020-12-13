from django.contrib import admin

from .models import Author, Category, Post, Comment, models
from tinymce.widgets import TinyMCE

class TinyMCEAdmin(admin.ModelAdmin):
    formfield_overides ={
        models.TextField: { 'widget': TinyMCE() }
    }

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post, TinyMCEAdmin)
