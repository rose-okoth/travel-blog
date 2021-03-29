from urllib.parse import quote_plus
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.db.models import Q
from django.utils import timezone
from django.contrib import messages
from .models import Post
from .forms import PostForm, RegistrationForm
from django.contrib.auth import authenticate, logout,login
from .email import send_welcome_email
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def post_create(request):
    # if not request.user.is_staff or not request.user.is_superuser:
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        #successful post message
        messages.success(request, "Post Successfully Created!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form":form,
    }
    return render(request,"post_form.html",context)

@login_required()
def post_detail(request,slug=None):
    instance = get_object_or_404(Post, slug=slug)
    # import pdb;pdb.set_trace()
    if instance.draft or instance.publish > datetime.datetime.now(timezone.utc):
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
            "title":instance.title,
            "instance":instance,
            "share_string":share_string
        }

    return render(request,"post_detail.html",context)

def post_list(request):
    today = timezone.now().date()
    # queryset_list = Post.objects.filter(draft=False).filter(publish__lte=timezone.now())
    queryset_list = Post.objects.active().order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query) 
            ).distinct()

    paginator = Paginator(queryset_list,5) #Show 5 contacts per page
    page_request_var = 'page'

    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        #if page not an integer, deliver first page
        queryset = paginator.page(1)
    except EmptyPage:
        #if page is out of range
        queryset = paginator.page(paginator.num_pages)

    context = {
            "object_list":queryset,
            "title":"List",
            "page_request_var":page_request_var,
            "today":today,
        }
    return render(request,"post_list.html", context)

@login_required()
def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Updated!")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "title":instance.title,
            "instance":instance,
            "form":form,
        }
    return render(request,"post_form.html",context) 

@login_required()
def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully Deleted!")
    return redirect("posts:home")

def post_signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)

        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data.get('password1')

            print(request.POST)

            user = authenticate(username=user.username, password=raw_password)
            name = request.POST["username"]
            email = request.POST["email"]
            send_welcome_email(name,email)
            # signin(request, user)

            return redirect("posts:home")

    else:
        form = RegistrationForm()

    return render(request, "signup.html", {"form": form})


def post_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    #   check credentials  
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:

                login(request, user)
                return redirect('posts:home')
            else:
                # login(request, user)
                return render(request, 'login.html', {"error": "Your account id is not active"})

        else:
            return render(request, 'login.html', {"error": "Invalid username or password"})

    return render(request, 'login.html')

def post_logout(request):
    logout(request)
    return redirect('posts:signin')
