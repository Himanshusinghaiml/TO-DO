from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.first_page,name='first'),
    path('todo-page/',views.todo_page,name='todo-page'),
    path('send-data/',views.senddata,name='send-data'),
    path('delete/<int:todo_id>/', views.delete_data, name='delete-data'),
    path('edit/<int:todo_id>/', views.edit_data, name='edit-data'),

    
]