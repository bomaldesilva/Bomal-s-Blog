from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request,'index.html',{'posts':post})
def post(request,pk):
    post = Post.objects.get(id=pk)
    return render(request,'post.html',{'post':post})