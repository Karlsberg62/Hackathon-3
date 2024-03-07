from django.urls import path
from . import views

urlpatterns = [
path('',views.index, name='index'),
path('post/', views.PostList.as_view(), name='posts')
]
