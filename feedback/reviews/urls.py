from django.urls import path
from . import views

urlpatterns = [
    path("",views.review,name="start-page"),
    path("thankyou",views.thankyou,name="thank-page"),
]
