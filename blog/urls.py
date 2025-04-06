from django.urls import path
from blog.views import *

app_name = "blog"
urlpatterns = [
    path("" , blog_page, name='index'),
    path("<int:pid>" , single_page ,name= 'single'),
    path('category/<str:cate>' , blog_page , name= 'category'),
    path("author/<str:author_user>" , blog_page , name= "author" ),
    path("search/" , search_view , name="search"),
]
