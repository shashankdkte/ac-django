from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect

monthly_challange_dict = {
  "january":"Wake up at 6:00 am",
  "february":"Go to Gym for 90 min",
  "march":"Practice React Projects",
  "april":"Complete Node Bootcamp",
  "may":"Read for 50 min",
  "june":"Drink 8 glasses water",
  "july":"Consume no sugar",
  "august":"Consume no Salt",
   "september":"Practise node",
  "november":"Practise aspnet",
  "november":"Practise algorithm",
  "december":"Practise flute",
}

# Create your views here.
def monthly_challange_number(request,month):
    months = list(monthly_challange_dict.keys())
    if month > len(months):
       return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]

    return HttpResponseRedirect("/challanges/" + redirect_month)


def monthly_challange(request,month):
  challange_text = None
  try:
     challange_text = monthly_challange_dict[month];
     return HttpResponse(challange_text)
  except: 
    return HttpResponseNotFound("You have entered wrong value")
     