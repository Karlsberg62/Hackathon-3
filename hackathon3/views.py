from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post 
from .forms import CommentForm

# Create your views here.
def index(request):
    return render(request,'hackathon3/index.html')

# Create your views here.
# class based view
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "hackathon3/index.html"
    paginate_by = 4
        #searchbar functionality
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            post = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(date__icontains=query) |
                Q(location__icontains=query)
            )
        else:
            post = self.model.objects.all()
        return post



## function based view
def PostDetail(request, slug):
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
    comments = post.comment.all().order_by("-created_on")
    comment_count = post.description.filter(approved=True).count()

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

    comment_form = CommentForm()
    

    return render(
        request,
        "hackathon3/post_detail.html",
        {
            "post": post, 
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )