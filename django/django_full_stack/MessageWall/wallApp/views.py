from django.shortcuts import render, redirect
from .models import User, UserManager, Message, Comment
from django.contrib import messages

# Create your views here.
# Route to send users to main page to either Login or 
# Register. Register is form/POST
def index(request):
    return render(request, "index.html")

    
def success(request):
    print(request.session['name'])
    if 'name' not in request.session:
        return redirect('/')
    
    # logged_user = User.objects.get(id=request.session['id'])
    context = {
        'user': User.objects.all(),
    }
    return render(request, 'success.html', context)

# POST data sent from registration form
#  (fname, lname, email, password, confpw)
def register(request):
    errors = User.objects.validator(request.POST)
    # If errors in form, display error message and redirect to index
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    # If not, add POST data and create user object. 
    # Redirect to index for now
    else:
        new_user = User.objects.register(request.POST)
        new_user.fname = new_user.fname.title()
        request.session['user_id'] = new_user.id
        request.session['name'] = new_user.fname
        messages.success(request, "You have successfully registered!")
        return redirect('/success')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, "Invalid Email or Password")
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    request.session['name'] = user.fname
    messages.success(request, "You have successfully logged in")
    return redirect('/success')

    # Not sure why the passwords weren't matching
    """
    # print(request.POST)
    # if request.method == "GET": # if GET then it's not from POST form
    #     redirect('/')
    if not User.objects.authenticate(
        request.POST['email'], request.POST['password']):
        messages.error(request, "Invalid Email/Password")
        return redirect('/')

    # curr_user = User.objects.filter(email=request.POST['email'])
    # if len(curr_user) > 0:
    #     curr_user = curr_user[0]
    #     breakpoint()
    m = User.objects.get(email=request.POST['email'])
    breakpoint()
    if m.password == request.POST['password']:
        request.session['user_id'] = m.id
        request.session['name'] = m.fname
        
        # print(curr_user)
        # if curr_user.password == request.POST['password']:
        #     request.session['id'] = curr_user.id
        #     print(request.session['id'])
        #     request.session['user'] = curr_user.fname
        #     messages.success(request, "You have successfully logged in/out")
        return redirect('/success')
    return redirect('/')
    """


def logout(request):
    try:
        del request.session['user_id']
        messages.success(request, "Successfully logged out")
    except KeyError:
        pass
    return redirect('/')

# GET - get all messages and send to the wall
def wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    
    context = {
        'all_messages': Message.objects.all().order_by('-created_at'),
    }
    return render(request, "thewall.html", context)

# POST - Retrieved by thewall.html
# Create message object and then redirect to 'wall' function
def postMessage(request):
    new_message = Message.objects.create(
        msg=request.POST['message'],
        user_msg=User.objects.get(id=request.session['user_id'])
    )
    return redirect('/wall')

def postComment(request, msgid):
    new_comment = Comment.objects.create(
        cmt = request.POST['comment'],
        user_cmt = User.objects.get(id=request.session['user_id']),
        msg_cmt = Message.objects.get(id=msgid)
    )
    return redirect('/wall')

def deleteComment(request, cmtid):
    comment_to_delete = Comment.objects.get(id=cmtid)
    comment_to_delete.delete()
    return redirect('/wall')


