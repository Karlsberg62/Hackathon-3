from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    """
    Form for adding a Post
    """

    class Meta:
        model = Post
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "meal_type",
            "cuisine_types",
            "calories",
        ]

        #ingredients = forms.CharField(widget=RichTextWidget())
        #instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }

        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Recipe Ingredients",
            "instructions": "Recipe Instructions",
            "image": "Recipe Image",
            "image_alt": "Describe Image",
            "meal_type": "Meal Type",
            "cuisine_types": "Cuisine Type",
            "calories": "Calories",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)