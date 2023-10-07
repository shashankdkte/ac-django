from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view(),name="start-page"),
    path("thankyou",views.ThankYouView.as_view(),name="thank-page"),
    path("review-list",views.ReviewListView.as_view(),name="review-list-page"),
    path("single-review-detail/<int:id>",views.SingleReviewView.as_view(),name="single-review-page"),
]
