from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone

# code for get time and use in blog_page

def blog_page(request):
    time_now=timezone.localtime(timezone.now())
    posts = Post.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    context = {"posts":posts}
    return render(request, "blog/blog-home.html" , context)

def single_page(request , pid):
    #post = Post.objects.get(id = pid)
    post = get_object_or_404(Post , pk=pid , status = 1)
    # create a def for count post views
    def addview(post):
        post.content_view += 1
        return post.save() 
    addview(post)
    context = {"post":post} 
    return render(request, "blog/blog-single.html" , context)

def test(request):
    #post = Post.objects.get(id = pid)
    post =  Post.objects.filter(status=1)
    context = {"posts":post}
    return render(request , "blog/test.html" , context)

