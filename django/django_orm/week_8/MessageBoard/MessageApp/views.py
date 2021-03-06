from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def root(request):
    context = {
        "Messages": Message.objects.all()
    }
    return render(request, 'home.html', context)

def newMessage(request):
    if request.method == "POST":
        newMessage = Message.objects.create(author=request.POST['author'],
            content=request.POST['content'])
        return redirect(f'/message/{newMessage.id}')
    else:
        return redirect('/')

def oneMessage(request, messageid):
    context = {
        'message': Message.objects.get(id=messageid),
    }
    return render(request, "one_message.html", context)

def addComment(request):
    
    new_comment = Comment.objects.create(author=request.POST['author'],
        content=request.POST['content'],
        originalMessage=Message.objects.get(id=request.POST['messageid']))
    print(new_comment)
    return redirect(f'message/{new_comment.originalMessage.id}')