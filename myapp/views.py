from django.shortcuts import render, HttpResponse
import requests, json


# Create your views here.
def json_list(request):
    url = 'https://api.covid19api.com/countries'
    res = requests.get(url).json()
   
    context = {
        "data": res,
        }
    return render(request, "json_output.html", context)