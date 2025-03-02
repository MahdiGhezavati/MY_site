from django.urls import path
from website.views import *

app_name = "website"
urlpatterns = [
    path("" , home_page, name="Index"),
    path("about-me" , about_page ,name= "About"),
    path("contact" , contact_page ,name= "Contact")
]
