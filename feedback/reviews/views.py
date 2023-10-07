from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
# Create your views here.



class ReviewView(View):
  def get(self,request):
    form  = ReviewForm()

    return render(request,"reviews/review.html",{
      "form": form
    })
  
  def post(self,request):
    form = ReviewForm(request.POST)

    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/thankyou")



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
  
