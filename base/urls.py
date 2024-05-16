from django.urls import path, reverse_lazy
#from . import views                 # For Functions, thus but now it's class so 
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage         # CLASSES FROM VIEWS FILES 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    #path('logout/', custom_logout, name='logout'),
    path('register/', RegisterPage.as_view(),name="register"),


    path('', TaskList.as_view(), name='tasks'),                             # root URL - #base url thus empty string, view name
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),               # when clicked on list item - sub url <int:pk> - pk - primary key  
    path('create-task/', TaskCreate.as_view(), name='task-create'),         # url accessed to create the task
    path('update-task/<int:pk>', TaskUpdate.as_view(), name='task-update'),         # url accessed to update the task
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='task-delete'),         # url accessed to delete the task
]