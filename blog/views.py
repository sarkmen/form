from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm1, PostForm2, CommentForm

# Create your views here.
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list' : post_list})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm2(request.POST, request.FILES)
        if form.is_valid():
            post=form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm2()
    return render(request, 'blog/post_form.html', {'form' : form, })


def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form' : form, })



def comment_detail(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    return render(request, 'blog/comment_detail.html', {'comment' : comment})