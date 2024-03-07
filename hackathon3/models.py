from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    """
    stores a single event post entry related to the :model:'auth.User'.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_posts')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    time = models.TimeField()
    location = models.CharField(max_length=200)
    max_attendees = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    image_alt_text = models.CharField(max_length=200, default='placeholder')
    max_attendees = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)  
    updated_on = models.DateTimeField(auto_now=True)
     

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return f"{self.title}| written by {self.author}"



class Comment(models.Model):
    """
    stores a single comment entry related to the :model:'auth.User' :model:'blog.Post'
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)   

    class Meta:
        ordering = ['created_on']
    def __str__(self):
        return f"Comment by {self.author} on {self.post}"



##class Hackathon3(models.Model):
##    title = models.CharField(max_length = 100)
##    image = CloudinaryField('image',default='placeholder')
