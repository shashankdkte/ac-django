from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view(),name="start-page"),
    path("thankyou",views.thankyou,name="thank-page"),
]
