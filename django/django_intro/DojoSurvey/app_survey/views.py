from django.shortcuts import render, HttpResponse, redirect
#from django.contrib import sessions
# Create your views here.
def index(request):
    return render(request, "index.html")

def survey(request):
    if request.method == "GET":
        return redirect('/')
    request.session['result'] = {
        'user_name': request.POST['user_name'],
        'location': request.POST['location'],
        'fav_lang': request.POST['fav_lang'],
        'comments': request.POST['comments'],
    }
    return redirect('/result')
    

def result(request):
    result = request.session['result']
    context = {'result': result}
    return render(request, 'result.html', context)