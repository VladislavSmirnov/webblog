from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import *
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, InvalidPage

page_el = 5

def index(request):
    return index_page(request, 1)

def index_page(request, page):
    p = Post.objects.order_by('create_date')
    posts = Paginator(p, page_el)
    return render(request, 'webblogs/index.html', {'page': posts.page(page), 'range': posts.page_range})


def detail(request, post_id):
    if request.method == 'POST':
        com = None if request.POST['id'] == 'None' else Comment.objects.get(pk=request.POST['id'])
        Comment(post=Post.objects.get(pk=post_id),comment=com, author=request.POST['author'], email=request.POST['email'], text=request.POST['text']).save()
        return HttpResponseRedirect('/'+post_id)
    post = Post.objects.get(id = post_id)
    return render(request, 'webblogs/detail.html', {'post': post})

def new_post(request):
    if request.method == 'POST':
        post = Post(author=request.POST['author'], text=request.POST['text'])
        post.save()
        return HttpResponseRedirect('/'+str(post.pk))
    return render(request, 'webblogs/new_post.html')

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.author = request.POST['author']
        post.text = request.POST['text']
        post.save()
        return HttpResponseRedirect('/' + post_id)
    return render(request, 'webblogs/edit.html', {'post': post})

def delete(request, post_id):
    if request.method == 'POST':
        Post.objects.get(pk = post_id).delete()
    return HttpResponseRedirect('/')

# Create your views here.
