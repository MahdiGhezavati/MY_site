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
    time_now=timezone.localtime(timezone.now())
    posts = Post.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    post = get_object_or_404(posts , pk=pid )
    
    # this section for next post and prev post for single page 
    posts= Post.objects.filter(poblished_date__lte=time_now ,status=1)           
    lis=[]      
    for index in posts:
        lis.append(index)
    list_next = []
    list_past = []
    for i in lis:
        if post.pk < i.pk:
            list_next.append(i)
        elif post.pk > i.pk:
            list_past.append(i)
    if list_next==[]:
        list_next.append(post)
    if list_past==[]:
        list_past.append(post)
    # end section
    list_past=list_past[-1]
    list_next=list_next[0]

    # create a def for count post views
    def addview(post):
        post.content_view += 1
        return post.save() 
    addview(post)
    context = {"post":post , "next":list_next , "past":list_past} 
    return render(request, "blog/blog-single.html" , context)

def test(request):
    #post = Post.objects.get(id = pid)
    post =  Post.objects.filter(status=1)
    context = {"posts":post}
    return render(request , "blog/test.html" , context)

