from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

def post_create(request):
    form = PostForm()
    context = {
        "form":form,
    }
    return render(request,"post_form.html",context)

def post_detail(request,id):
    instance = get_object_or_404(Post, id=id)
    context = {
            "title":instance.title,
            "instance":instance
        }

    return render(request,"post_detail.html",context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
            "object_list":queryset,
            "title":"List"
        }

    # if request.user.is_authenticated():
    #     context = {
    #         "title":"My List"
    #     }
    # else:
    #     context = {
    #         "title":"List"
    #     }
    return render(request,"index.html",context)
    
def post_update(request):
    return HttpResponse("<h1>Update</h1>")
    
def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")