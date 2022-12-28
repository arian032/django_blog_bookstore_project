from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BlogPost
from .forms import CommentForm


class PostListView(generic.ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'


def post_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    post_comment = post.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = post
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post_detail.html',
                  {'post': post,
                   'comments': post_comment,
                   'comment_form': comment_form
                   })


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = BlogPost
    fields = ['title', 'author', 'description']
    template_name = 'blog/post_update.html'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = BlogPost
    fields = ['title', 'author', 'description']
    template_name = 'blog/post_create.html'


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = BlogPost
    template_name = 'blog/post_delete.html'
    reverse_lazy('home')
