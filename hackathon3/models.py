from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    """
    stores a single event post entry related to the :model:'auth.User'.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_posts')
    category = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    excerpt = models.TextField(max_length=500,blank=True)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    max_attendees = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=200, default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)  
    updated_on = models.DateTimeField(auto_now=True)
     
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return f"{self.title}| written by {self.author}"


