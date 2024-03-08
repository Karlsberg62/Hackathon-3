from django.views.generic import (
    CreateView, ListView, 
    DetailView, DeleteView,
    UpdateView
)

from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Post
from .forms import EventForm, CommentForm

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

class update_event(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name = 'hackathon3/update_event.html'
    model = Post
    form_class = EventForm
    success_url = '/post/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class delete_event(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/post/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "hackathon3/post.html"
    paginate_by = 4


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    
    return render(
        request,
        "hackathon3/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }
    )    

