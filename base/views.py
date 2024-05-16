from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView  #description pane
from django.views.generic.edit  import CreateView, UpdateView, DeleteView, FormView   # create form; update  prefill and modify the data
from django.urls import reverse_lazy                # redirects user to certain part or page

from django.contrib.auth.views import LoginView                 
from django.contrib.auth.mixins import LoginRequiredMixin       #add this before builtin view to prevent unauthorised user accessing data, 
from django.contrib.auth.forms import UserCreationForm          #built in user creation
from django.contrib.auth import login,logout                           #to login user automatically once registered

from .models import Task

# Create your views here.

#if not logged in then restrict people from seeing it 


#gatekeeper thus on top - login optionality 
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True                     #--- unauthenticated users to be redirected 
    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'                         
    form_class = UserCreationForm                           #--- passing prebuilt form
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')                     #--- redirect on success when registered

    def form_valid(self, form):                         #-- the form submission is valid by rules
        user = form.save()                              #-- save the user
        if user is not None:                            #-- is user is suceesfully created
            login(self.request, user)                   #-- redirect control to login function for autologin
        return super().form_valid(form)
    
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:          
            return redirect('tasks')                    # if authenticated in a session -> no register page accessible
        return super().get(*args,**kwargs)              # if not authenticated continue doing whatever it is you were doing

#function based view
"""def taskList(request):
    return HttpResponse('To Do List')"""

#class based views 
class TaskList( LoginRequiredMixin , ListView):                   # Listeview return a template with query set of data
    model = Task
    context_object_name = 'tasks'           # to assign variable context in HTML / simple view


    #tasks displayed are only user's tasks who is authenticated, basically item ownership 
    def get_context_data(self, **kwargs ):          
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)          #filter all tasks based on user
        context['count'] = context['tasks'].filter(complete=False).count()          #output of incomplete tasks
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        return context

# detail view - when people click on an html item in for we display that particular view 
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'    # so we don't have to name is task_details.html default in django

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # by default createview gives model form to work with 
    # representation of form based on model -> takes model and create all fields by default
#   fields = ['title','description' etc]        instead using __all__
#    fields ='__all__'                          after implemetnting user based data 
    fields = ['title','description','complete']

    #redirect user after submission to different page -> add it to createview
    success_url = reverse_lazy('tasks')
     
    def form_valid(self, form):                              #set default value in creating task instead of selecting any user
            form.instance.user = self.request.user
            return super().form_valid(form)

# create view
# set model
# set fields
# set redirect value

class TaskUpdate(LoginRequiredMixin, UpdateView):                               #to update tasks
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):                               #to delete the task 
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')