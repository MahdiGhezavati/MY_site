from django.urls import path
from blog.views import *

app_name = "blog"
urlpatterns = [
    path("" , blog_page, name='index'),
    path("<int:pid>" , single_page ,name= 'single'),
]
