from django.shortcuts import render
from django.views import generic
from .models import Post
# Create your views here.
def index(request):
    return render(request,'hackathon3/index.html')

class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
    """
    
    queryset = Post.objects.filter(status=1)
    template_name = "hackathon3/post.html"
    paginate_by = 4