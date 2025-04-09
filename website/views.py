from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from website.forms import Contactform , newsletterform
from django.contrib import messages

def home_page(request):
    return render(request, "website/index.html")

def about_page(request):
    return render(request, "website/about.html")

def contact_page(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , " SUBMITED!")

    form = Contactform()
    return render(request ,"website/contact.html" , {"form":form })

def newsletter_page(request):
    if request.method == "POST":
        form = newsletterform(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


