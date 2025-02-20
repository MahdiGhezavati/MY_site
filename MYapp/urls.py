from django.urls import path
from MYapp.views import *

urlpatterns = [
    path("home" , homepage),
    path("about-me" , mepage)
]
