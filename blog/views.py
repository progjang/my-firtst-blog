from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.http import Http404
# Create your views here.
def index(request):
    pass

def post_list(request):
    qs = Post.objects.all()
    qs = qs.order_by('published_date')
    return render(request, 'blog/post_list.html', {
        'post_list': qs
    })

def post_detail(request,pk):
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404 # Page Not Found
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })
#@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {
        'form' : form,
    })

def post_edit(request,pk):
    # try:
    #     post = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    #     raise Http404 # Page Not Found
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form' : form
    })