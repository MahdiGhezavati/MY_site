from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect

def comingsoon(request):
    return render(request , 'comingsoon.html')