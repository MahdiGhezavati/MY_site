from django import template
from blog.models import Post
from django.utils import timezone

register = template.Library()

@register.inclusion_tag("website/lates_posts.html")
def latesposts ():
    time_now=timezone.localtime(timezone.now())
    posts = Post.objects.filter(poblished_date__lte=time_now ,status=1).order_by("poblished_date")[:6]
    print(posts)
    return {"posts":posts}