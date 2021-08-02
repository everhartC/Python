from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Shows

# Create your views here.
def home(request):
    return redirect('/shows')

def AddNewShow(request): #GET / RECEIVE db information from HTML form
    context = {
        "shows": Shows.objects.all()
    }
    return render(request, "add_show.html", context)

def CreateNewShow(request): #POST the data into a new html
    errors = Shows.objects.show_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/shows/new")
    else:    
        show = Shows.objects.create(title = request.POST['title'], network = request.POST['network'], 
            release_date = request.POST['reldate'], desc = request.POST['desc'])
        newShow_ID = show.id
        messages.success(request, "New Show successfully added")
    return redirect(f"/shows/{newShow_ID}")

def TvShow(request, id): #GET
    context = {
        "show": Shows.objects.get(id=id)
    }
    messages.success(request, "Show successfully updated")
    return render(request, "tv_show.html", context)

def AllShows(request): #GET shows
    context = {
        "shows": Shows.objects.all()
    }
    return render(request, "all_shows.html", context)

def EditShow(request, id):
    context = {
        "show": Shows.objects.get(id=id),
    }
    return render(request, 'edit_show.html', context)

def UpdateShow(request, id):
    errors = Shows.objects.show_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Shows.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['reldate']
        show.desc = request.POST['desc']
        show.save()
    return redirect(f'/shows/{id}')

def DeleteShow(request, id):
    show = Shows.objects.get(id=id)
    show.delete()
    return redirect('/shows')