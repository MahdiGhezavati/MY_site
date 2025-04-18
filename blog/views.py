from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from blog.models import Post ,Comments
from blog.forms import Commentform
from django.utils import timezone
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from django.contrib import messages
# code for get time and use in blog_page

def blog_page(request , cate=None , author_user=None , tag=None):
    time_now=timezone.localtime(timezone.now())
    posts = Post.objects.filter(poblished_date__lte=time_now , status = 1 )
    if cate:
        posts = posts.filter(category__name=cate)
    if author_user:
        posts = posts.filter(author__username = author_user)
    if tag:
        posts = posts.filter(tags__name=tag)
    
    posts = Paginator(posts , 2)
    try:
        page_number=request.GET.get('page')
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.get_page(1)
    except PageNotAnInteger:
        posts = posts.get_page(1)

    context = {"posts":posts}
    return render(request, "blog/blog-home.html" , context)

def single_page(request , pid):
    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , " SUBMITED! " , extra_tags="succ")
        else:
            messages.add_message(request , messages.ERROR , "plaese try again ! " , extra_tags="error")
    form = Commentform()
    #post = Post.objects.get(id = pid)
    time_now=timezone.localtime(timezone.now())
    posts = Post.objects.filter(poblished_date__lte=time_now , status = 1 ) 
    post = get_object_or_404(posts , pk=pid )
    # get comments
    comments = Comments.objects.filter(post=post.id , approved=True)
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
    context = {"post":post , "comments":comments , "form":form ,"next":list_next , "past":list_past} 
    return render(request, "blog/blog-single.html" , context)

def search_view(request):
    posts = Post.objects.filter(status=1)
    if request.method == "GET":
        posts = posts.filter(content__contains = request.GET.get("s"))
    context = {"posts":posts}
    return render(request , "blog/blog-home.html" ,context)






# secend way for get post categorys
#def category_page(request , cate):
    #osts = Post.objects.filter(status=1)
    #posts = posts.filter(category__name=cate)
    #context = {"posts":posts}
    #return render(request , "blog/blog-home.html" , context)
