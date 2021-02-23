from django.shortcuts import render, HttpResponse
#from time import gmtime, strftime
from datetime import date

today = date.today()

# Create your views here.
def index(request):
    context = {
        "time": today.strftime(R"%m/%d/%Y")
    }
    return render(request, 'index.html', context)