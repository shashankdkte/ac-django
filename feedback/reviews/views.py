from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView
# Create your views here.



class ReviewView(CreateView):
 model = Review
 form_class = ReviewForm
 template_name = "reviews/review.html"
 success_url = "/thankyou"



class ThankYouView(TemplateView):
  template_name ="reviews/thankyou.html"

  def get_context_data(self, **kwargs: Any):
    context = super().get_context_data(**kwargs)
    context["message"] = "This works!"
    return context
  

class ReviewListView(ListView):
  template_name="reviews/review_list.html"
  model = Review
  context_object_name = "reviews"

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data  
  
class SingleReviewView(DetailView):
  template_name = "reviews/single-review-detail.html"
  model  = Review
  
  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      loaded_review = self.object
      request = self.request
      fav = request.session.get("fav")
      context["fav"] = fav == str(loaded_review.id)
      return context
  

class AddFavouriteView(View):
  def post(self,request):
    review_id = request.POST["review_id"]
    request.session["fav"] = review_id
    return  HttpResponseRedirect("/single-review-detail/" + review_id)