from django import forms
from django.forms import ModelForm
from .models import Post



class EventForm(forms.ModelForm):
    """
    Form for adding a recipe
    """
    class Meta:
        model = Post
        fields = [
            "title",
            "category",
            "description",
            "excerpt",
            "date",
            "time",
            "location",
            "max_attendees",
            "featured_image",
        ]
        
        
        labels = {
            "title": "Event Title",
            "category": "Category",
            "description": "Description",
            "excerpt": "Excerpt",
            "date": "Date",
            "time": "Time",
            "location": "Location",
            "max_attendees": "Max Attendees",
            "featured_image": "Featured Image",
        }
        def save(self, commit=True, author=None):
            instance = super().save(commit=False)
            if author:
                instance.author = author
            if commit:
                instance.save()
            return instance