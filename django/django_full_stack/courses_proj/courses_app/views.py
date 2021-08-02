from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def home(request): #GET Retrieves all objects stored in the Course DB and renders them to homepage.html
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'homepage.html', context)

# POST Get all of the form data from homepage and 
# redirect back to homepage to display new information
def addCourse(request): 
    errors = Course.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        new_course = Course.objects.create(name=request.POST['name'])
        new_course_desc = Description.objects.create(content=request.POST['desc'])
        new_course.desc = new_course_desc
        new_course.save()
    return redirect('/')


def deleteCourse(request, courseID):
    if request.method == "GET":
        context = {
            'course': Course.objects.get(id=courseID)
        }
        return render(request, 'delete.html', context)

    if request.method == "POST":
        course_to_del = Course.objects.get(id=courseID)
        course_to_del.delete()
    return redirect('/')