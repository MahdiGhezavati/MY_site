from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("this is a personal page and \n<h1>Home Page <h1>")
def about_page(request):
    return HttpResponse("Mahdi ghzavati \n im mahdi and live in iran \n my id in telegram app = @ImahdiI")