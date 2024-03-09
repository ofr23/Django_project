from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from movie.models import Movie,Rating, Actor,Genre

def index(request):
    if request.method == 'POST':
        # Process the form data if needed
        # For now, let's just redirect to movielist.html
        return HttpResponseRedirect('/show')
    return render(request, 'index.html')

def show(request):
    # dictionary for passing data to movielist.html file
    alldata=Movie.objects.all()
    data={
       'alldata':alldata
    }
     

    
    return render(request, 'movielist.html', data)
