from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Task

# Create your views here.

#function based view
"""def taskList(request):
    return HttpResponse('To Do List')"""

#class based views 
class TaskList(ListView):                   # Listeview return a template with query set of data
    model = Task
    context_object_name = 'tasks'           # to assign variable context in HTML / simple view

    # detail view - when people click on an html item in for we display that particular view 

class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'    # so we don't have to name is task_details.html default in django