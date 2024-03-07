from django.urls import path
from . import views
from .views import PostList, PostDetail 

urlpatterns = [
    #path('',views.index, name='index')
    path('post/', PostList.as_view(), name='index'),
    path('post/<slug:pk>/', PostDetail.as_view(), name='post_detail'),
]
