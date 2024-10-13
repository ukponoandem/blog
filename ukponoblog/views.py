from django.shortcuts import render
from .models import blogs
# Create your views here.
def index(request):
    Blogs = blogs.objects.all()
    return render(request,'index.html' ,{'Blogs': Blogs})



def blog (request,pk):
    bloga = blogs.objects.get(id=pk)
    return render(request,"blog.html",{"bloga" : bloga} )