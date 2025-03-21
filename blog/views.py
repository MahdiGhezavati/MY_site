from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from blog.models import Post


def blog_page(request):
    posts = Post.objects.filter(status = 1)
    context = {"posts":posts}
    return render(request, "blog/blog-home.html" , context)

def single_page(request , pid):
    #post = Post.objects.get(id = pid)
    post = get_object_or_404(Post , pk=pid)
    context = {"post":post}
    return render(request, "blog/blog-single.html" , context)

def test(request,pid):
    #post = Post.objects.get(id = pid)
    post = get_object_or_404(Post , pk=pid)
    context = {"post":post}
    return render(request , "blog/test.html")



