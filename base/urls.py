from django.urls import path
#from . import views                 # For Functions, thus but now it's class so 
from .views import TaskList

"""urlpatterns = [
    path('', views.taskList, name='tasks'),            #base url thus empty string, view name
]"""

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),            #
]