from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Tag,Author,Post
all_posts = [
   {
      "name":"The Garden Resort",
      "image":"001-garden.svg",
      "content":"This is a dummy blog content site for getting dummy information.Please have a look",
      "date":date(2021,7,29),
      "fullContent":"",
      "slug":"garden-resort"
   },
     {
      "name":"The Hill Resort",
      "image":"006-landscape.svg",
      "content":"This is a dummy blog content site for getting dummy information.Please have a look",
      "date":date(2021,7,28),
      "fullContent":"",
      "slug":"hill-resort"

   },
     {
      "name":"The Hot  Balloon",
      "image":"014-hotairballoon.svg",
      "content":"This is a dummy blog content site for getting dummy information.Please have a look",
      "date":date(2021,7,27),
      "fullContent":"",
      "slug":"hot-balloon"

   },
  {
      "name":"The Rainbow",
      "image":"023-rainbow.svg",
      "content":"This is a dummy blog content site for getting dummy information.Please have a look",
      "date":date(2021,7,26),
      "fullContent":"",
      "slug":"rainbow-resort"

   },
     {
      "name":"The Windmill Resort",
      "image":"028-windmill.svg",
      "content":"This is a dummy blog content site for getting dummy information.Please have a look",
      "date":date(2021,7,25),
      "fullContent":"",
      "slug":"windmill-resort"

   }
]

def get_date(post):
  return post['date']
# Create your views here.
def starting_page(request):
  sorted_posts = sorted(all_posts, key=get_date);
  sorted_posts = Post.objects.all().order_by("-date")[:3]
  return render(request, "blog/index.html",{
     "latest_posts":sorted_posts
  })


def posts(request):
  latest_posts = Post.objects.all().order_by("-title")
  return render(request, "blog/all_posts.html",{
     "latest_posts":latest_posts
  })


def post_detail(request,slug):
    
    identified_post =Post.objects.get(slug = slug)
    return render(request, "blog/single-post-detail.html", {
       "post":identified_post,
       "tags":identified_post.tags.all()
    })
