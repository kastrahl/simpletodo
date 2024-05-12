from django.urls import path
#from . import views                 # For Functions, thus but now it's class so 
from .views import TaskList, TaskDetail

"""urlpatterns = [
    path('', views.taskList, name='tasks'),            #base url thus empty string, view name
]"""

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),         # root URL - 
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),   # when clicked on list item - sub url <int:pk> - pk - primary key  
]