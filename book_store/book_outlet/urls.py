from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="start-page"),
    path("book-detail/<int:id>",views.book_detail,name="book-detail"),
]
