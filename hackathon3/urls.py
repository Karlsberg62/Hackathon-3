from django.urls import path
from . import views

urlpatterns = [
path('',views.index, name='home'),
path('post/', views.PostList.as_view(), name='posts'),
path('profile/', views.profile, name="profile"),
path('<slug:slug>/', views.post_detail, name='post_detail'),
path('make_event', views.make_event.as_view(), name='make_event'),
path('<slug:slug>/update/', views.update_event.as_view(), name='update_event'),
path('<slug:slug>/delete/', views.delete_event.as_view(), name='delete_event')
]
