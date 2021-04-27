from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from .forms import CommentForm


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['commentform'] = CommentForm()
        return context

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.filter(active=True)

        new_comment = None

        # Comment posted
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)

            if comment_form.is_valid():

                # Create Comment object
                new_comment = comment_form.save(commit=False)

                # Assign the current post to the comment
                new_comment.post = post

                # Save the comment to the database
                new_comment.save()

        else:
            comment_form = CommentForm()

        return render(request, 'post_detail.html', {'post': post,
                                                    'comments': comments,
                                                    'new_comment': new_comment,
                                                    'comment_form': comment_form})


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title', 'body']


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
