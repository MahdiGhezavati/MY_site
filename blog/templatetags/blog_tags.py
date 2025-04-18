from django import template
from blog.models import Post , Comments
from blog.models import category

register = template.Library()

@register.inclusion_tag("blog/sidebar/popular_post.html")
def latesposts ():
    posts = Post.objects.filter(status=1).order_by("poblished_date")[:3]
    return {"posts":posts}  

@register.simple_tag(name="comments_count")
def function(pid):
    return Comments.objects.filter(post=pid , approved=True).count()


@register.inclusion_tag("blog/sidebar/category.html")
def postcategory():
    posts = Post.objects.filter(status=1)
    cate = category.objects.all()
    category_dict = {}
    for name in cate:
        category_dict[name]=posts.filter(category=name).count()
    return {"category":category_dict}