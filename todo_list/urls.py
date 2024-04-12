from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.first_page.as_view(),name='first'),
    path('todo_page/',views.todo_page.as_view(),name='todo-page'),
    path('send_data/',views.SendDataApi.as_view(),name='send-data'),
    
    path('delete/<int:todo_id>/', views.delete_data, name='delete-data'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit-data'),
       
]