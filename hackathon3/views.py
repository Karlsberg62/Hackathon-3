from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Post

# Create your views here.
def index(request):
    return render(request,'hackathon3/index.html')

def profile(request):
    return render(request,'hackathon3/profile.html')

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

    """
    #searchbar functionality
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            posts = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(location__icontains=query) |
                Q(date__icontains=query) |
                Q(category__icontains=query) |
                Q(excerpt__icontains=query)
            )
        else:
            posts = self.model.objects.all()
        return posts
    """

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
        An instance of :model:`blog.Post`.
     ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    **Template:**
    :template:`blog/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    # this is a shortcut to get data or raise a https404error # same as render being a shortcut to load data to a templ and return it.
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "hackathon3/post_detail.html",
        {
            "post": post,
        },
    )
