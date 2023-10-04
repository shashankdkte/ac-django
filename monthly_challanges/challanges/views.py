from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound

# Create your views here.
def monthly_challange(request,month):
  challange_text = None
  if month == "january":
    challange_text = "Walk 20 min everyday"
  elif month == "february":
    challange_text = "Learn HTML CSS"
  elif month == "march":
    challange_text = "Learn Django"
  else:
    return HttpResponseNotFound("You have entered wrong value")
  return HttpResponse(challange_text)