from django.urls import path
from . import views

urlpatterns = [
    path("", views.index,name="index"),
    path("allpost",views.allpostpage,name="allposts"),
    path("allpost/<slug:slug>",views.singlepost,name="mypost")
]
