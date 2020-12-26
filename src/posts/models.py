from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField

from decimal import Decimal

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

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add = True)
    content = models.TextField(default = "")
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    restaurant_name = models.TextField()
    overview = models.TextField()
    food_rating = models.DecimalField(max_digits=3, decimal_places=1)
    atmosphere_rating = models.DecimalField(max_digits=3, decimal_places=1)
    hospitality_rating = models.DecimalField(max_digits=3, decimal_places=1)
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add = True)
    location = models.TextField(default = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d424146.1026392451!2d150.65179666970943!3d-33.847356724710885!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b129838f39a743f%3A0x3017d681632a850!2sSydney%20NSW!5e0!3m2!1sen!2sau!4v1607782680258!5m2!1sen!2sau") # Map of Sydney
    latitude = models.DecimalField(max_digits=17, decimal_places=14, default=-33.865143)
    longitude = models.DecimalField(max_digits=18, decimal_places=14, default=151.209900)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    image = models.FileField(blank=True)
    featured = models.BooleanField(default = True)
    announcement = models.BooleanField(default = False)
    

    def __str__(self):
        return self.title

    def post_url(self):
        return reverse('post_detail', kwargs={
            'id': self.id
        })

    def getTotalScore(self):
        return (self.food_rating*Decimal('0.8') + self.atmosphere_rating*Decimal('0.1') + self.hospitality_rating*Decimal('0.1'))
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title