from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todomodel
from django.shortcuts import get_object_or_404, render

 
def first_page(req):
    return render(req,'index.html')

def todo_page(req):
    all_data=Todomodel.objects.all()
    return render(req, 'todo.html', {'all_data': all_data})

def senddata(req):
    if req.method == 'POST':
        title = req.POST.get('title')  # Use req.POST.get() to retrieve POST data
        description = req.POST.get('description')

        # Create a new TodoModel object and save it to the database
        new_todo = Todomodel(Title=title, Description=description)
        new_todo.save()

        # return  render(req,'todo.html') 
    return redirect('todo-page')

 
def delete_data(req, todo_id):
    if req.method == 'POST':
        todo_item = get_object_or_404(Todomodel, id=todo_id)
        todo_item.delete()
        return redirect('todo-page')  
    else:
        return HttpResponse('Only POST requests are allowed')
  

def edit_data(req, todo_id):
     
    todo_item = get_object_or_404(Todomodel, id=todo_id)
    if req.method == 'POST':
        # Get the updated data from the form
        title = req.POST.get('title')
        description = req.POST.get('description')

        # Update the todo item with the new data
        todo_item.Title = title
        todo_item.Description = description
        todo_item.save()
    return redirect('todo-page')   

  