from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Task

# Create your views here.

#function based view
"""def taskList(request):
    return HttpResponse('To Do List')"""

#class based views 
class TaskList(ListView):                   #Listeview return a template with query set of data
    model = Task