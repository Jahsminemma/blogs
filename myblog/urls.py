from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, SignUpView
urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home"),
    path("post/new", BlogCreateView.as_view(), name="post_new"),
    path('post/edit/<int:pk>/', BlogUpdateView.as_view(), name="post_update"),
    path('signup/', SignUpView.as_view(), name='signup')
]
