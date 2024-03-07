from django.views.generic import (
    CreateView, ListView, 
    DetailView, DeleteView,
    UpdateView
)

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import EventForm

# Create your views here.
def index(request):
    return render(request,'hackathon3/index.html')

def profile(request):
    return render(request,'hackathon3/profile.html')

class make_event(LoginRequiredMixin, CreateView):
    template_name = 'hackathon3/make_event.html'
    model = Post
    form_class = EventForm
    success_url = '/post/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # form.instance.user = self.request.user        
        # return super(make_event, self).form_valid(form)
    

class PostList(generic.ListView):
    """
    Returns all published posts in :model:`hackathon3.Post`
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
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    

    return render(
        request,
        "hackathon3/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        }
    )    

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


