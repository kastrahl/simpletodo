from django.urls import path
#from . import views                 # For Functions, thus but now it's class so 
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete         # CLASSES FROM VIEWS FILES 

"""urlpatterns = [
    path('', views.taskList, name='tasks'),            #base url thus empty string, view name
]"""

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),         # root URL - 
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),   # when clicked on list item - sub url <int:pk> - pk - primary key  
    path('create-task/', TaskCreate.as_view(), name='task-create'),         # url accessed to create the task
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='task-update'),         # url accessed to update the task
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='task-delete'),         # url accessed to delete the task

]