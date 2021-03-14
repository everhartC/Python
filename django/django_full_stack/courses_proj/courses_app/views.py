from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'all_courses': Courses.objects.all()
    }

    return render(request, 'index.html', context)

def addCourse(request):
    errors = Courses.objects.course_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        course = Courses.objects.create(name=request.POST['name'])
        desc = Description.objects.create(content=request.POST['desc'])
        course.desc = desc
        course.save()
    
    return redirect('/courses')

def destroyCourse(request, courseID):
    if request.method == 'GET':
        context = {
            'course': Courses.objects.get(id=courseID)
        }
        return render(request, 'remove_course.html', context)

    if request.method == 'POST':
        course = Courses.objects.get(id=courseID)
        course.delete()
        return redirect('/courses')

def comments(request, courseID):
    context = {
        'course': Courses.objects.get(id=courseID)
    }
    return render(request, 'comments.html', context)

def addComment(request, courseID):
    Comment.objects.create(content=request.POST['content'], 
        course=Courses.objects.get(id=courseID))
    return redirect(f"/courses/{courseID}")
