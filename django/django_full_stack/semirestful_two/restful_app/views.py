from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def myRedirect(request):
    return redirect('/shows')

def index(request):  # GET - returns a template that displays ALL the shows in a table
    context = {
        'all_shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def addNewShow(request):  # GET - returns a template containing the form for adding a new TV Show
    return render(request, 'newShow.html')

def createShow(request):  # Handles data from newShow.html and redirects to shows page with new shows info
    newtitle = request.POST['title']
    newnetwork = request.POST['network']
    newdesc = request.POST['desc']
    new_show = Show.objects.create(title=newtitle, network=newnetwork, desc=newdesc)
    return redirect(f'/shows/{new_show.id}')

def showPage(request, showID):
    context = {
        'show': Show.objects.get(id=showID)
    }
    return render(request, 'show.html', context)

def editShow(request, showID):   #GET returns a template with form to edit show
    context = {
        'show': Show.objects.get(id=showID)
    }
    return render(request, 'editShow.html', context)

def updateShow(request, showID):
    edited_show = Show.objects.get(id=showID)
    edited_show.title = request.POST['title']
    edited_show.network = request.POST['network']
    edited_show.reldate = request.POST['reldate']
    edited_show.desc = request.POST['desc']
    edited_show.save()
    return redirect(f'/shows/{edited_show.id}')

def deleteShow(request, showID):
    show_to_delete = Show.objects.get(id=showID)
    show_to_delete.delete()
    return redirect('/shows')