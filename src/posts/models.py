from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True)
    location = models.TextField(default = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d424146.1026392451!2d150.65179666970943!3d-33.847356724710885!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b129838f39a743f%3A0x3017d681632a850!2sSydney%20NSW!5e0!3m2!1sen!2sau!4v1607782680258!5m2!1sen!2sau") # Map of Sydney
    comment_count = models.IntegerField(default = 0)
    view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default = True)

    def __str__(self):
        return self.title

    def post_url(self):
        return reverse('post_detail', kwargs={
            'id': self.id
        })