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
    category = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    max_attendees = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=200, default='placeholder')
    max_attendees = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)  
    updated_on = models.DateTimeField(auto_now=True)
     

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return f"{self.title}| written by {self.author}"


