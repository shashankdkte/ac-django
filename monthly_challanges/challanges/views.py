from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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

def index(request):
   months = list(monthly_challange_dict.keys())
   return render(request,"challanges/index.html", {
      "months": months
   })

def monthly_challange_number(request,month):
    months = list(monthly_challange_dict.keys())
    if month > len(months):
       return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challange", args=[redirect_month]) #
    return HttpResponseRedirect(redirect_path)


def monthly_challange(request,month):
  challange_text = None
  try:
     challange_text = monthly_challange_dict[month];
     return render(request, "challanges/challange.html",{
        "text": challange_text,
        "month_name":month
     })
  except: 
    return HttpResponseNotFound("You have entered wrong value")
     