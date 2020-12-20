from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField

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

class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    food_rating = models.DecimalField(max_digits=3, decimal_places=1)
    atmosphere_rating = models.DecimalField(max_digits=3, decimal_places=1)
    hospitality_rating = models.DecimalField(max_digits=3, decimal_places=1)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now_add = True)
    location = models.TextField(default = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d424146.1026392451!2d150.65179666970943!3d-33.847356724710885!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x6b129838f39a743f%3A0x3017d681632a850!2sSydney%20NSW!5e0!3m2!1sen!2sau!4v1607782680258!5m2!1sen!2sau") # Map of Sydney
    coord = models.ForeignKey('Location', on_delete=models.CASCADE)
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
    
    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()