from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(),name="starting-page"),
    path("posts",views.AllPostsView.as_view(),name="posts-page"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(),name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later"),
]
# http://127.0.0.1:8000/posts/trouble-with-bliss-the
# http://127.0.0.1:8000/posts/trouble-with-bliss-the