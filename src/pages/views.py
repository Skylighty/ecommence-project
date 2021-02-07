from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# Place that holds various pages of the website
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {}) # HTML String 
