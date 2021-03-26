from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create</h1>")

def post_detail(request):
    return HttpResponse("<h1>Detail</h1>")

def post_list(request):
    return HttpResponse("<h1>List</h1>")
    
def post_update(request):
    return HttpResponse("<h1>Update</h1>")
    
def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")