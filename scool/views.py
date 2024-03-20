from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Person, Course, Grade

def index(request):
    # return HttpResponse('Hello')
    persons = Person.objects.all()
    courses = Course.objects.all()
    grades = Grade.objects.all()

    #return render(request, '1.html', {'data':'Hello'})  
    return render(request, 'view_data.html', {'persons': persons, 'courses': courses, 'grades': grades})

def persons(r, id):
    if id:
        person = Person.objects.get(id=id)
        return render(r, 'person.html', {'student':person})
    
    data = Person.objects.all()
    return render(r, 'persons.html', {'students':data})