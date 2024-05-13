from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView  #description pane
from django.views.generic.edit  import CreateView, UpdateView, DeleteView   # create form; update  prefill and modify the data
from django.urls import reverse_lazy                # redirects user to certain part or page

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

class TaskCreate(CreateView):
    model = Task
    # by default createview gives model form to work with 
    # representation of form based on model -> takes model and create all fields by default
#   fields = ['title','description' etc]        instead use __all__
    fields ='__all__'
    #redirect user after submission to different page -> add it to createview
    success_url = reverse_lazy('tasks')

# create view
# set model
# set fields
# set redirect value 

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')