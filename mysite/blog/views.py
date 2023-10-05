from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starting_page(request):
  return render(request, "blog/index.html")

def posts(request):
  return HttpResponse("PostsPage")

def post_detail(request,slug):
  return HttpResponse(f"Postdetail {slug}")