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
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)  
    update_on = models.DateTimeField(auto_now=True)
     

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return f"{self.title}| written by {self.author}"






##class Hackathon3(models.Model):
##    title = models.CharField(max_length = 100)
##    image = CloudinaryField('image',default='placeholder')
