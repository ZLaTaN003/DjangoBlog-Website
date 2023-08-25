from django.shortcuts import render
from django.http import Http404
from myapp.models import Post


# Create your views here.

def index(request):
    latestposts = Post.objects.all().order_by("-date")[:2]
    return render(request,"myapp/index.html",{
        "latestpost" : latestposts
    })


def allpostpage(request):
    allpost = Post.objects.all().order_by("-date")
    return render(request,"myapp/allpost.html",{
        "allpost" : allpost
    })



def singlepost(request,slug):
    
      identifiedpost = Post.objects.get(slug=slug)
      return render(request,"myapp/mypost.html",{
           "identifiedpost" : identifiedpost
      })
