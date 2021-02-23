from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'homePage.html')

def formSubmission(request):
    request.session['email'] = request.POST['email']
    request.session['name'] = request.POST['name']
    request.session['numberoftickets'] = request.POST['numberoftickets']

    return redirect('/userTicketSale')

def user(request):
    context = {
        'email': request.session['email'],
        'name': request.session['name'],
        'numberoftickets': request.session['numberoftickets'],
    }
    return render(request, 'user.html', context)

def fourOfour(request, Anything):
    return HttpResponse("nothing here")