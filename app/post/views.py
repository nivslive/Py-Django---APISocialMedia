from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # defina o autor com o usuário logado
            post.save()
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm()

    return render(request, 'post_create.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return HttpResponseRedirect('/posts/')


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # defina o autor com o usuário logado
            post.save()
            return HttpResponseRedirect('/posts/')
    else:
        form = PostForm(instance=post)

    return render(request, 'post_update.html', {'form': form})