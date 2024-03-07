from django.urls import path
from . import views

urlpatterns = [
path('',views.index, name='index'),
path('post/', views.PostList.as_view(), name='posts'),
path('profile/', views.profile, name="profile"),
path('<slug:slug>/', views.post_detail, name='post_detail'),
path('make_event', views.make_event.as_view(), name='make-event')
]
