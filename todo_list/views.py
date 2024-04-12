from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todomodel
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodomodelSerializer
from rest_framework import status

class first_page(APIView):
    def get(self,request):
        return render(request,'index.html')

 
class todo_page(APIView):
    def get(self,request):
        return render(request,'todo.html')


class SendDataApi(APIView):
    # serializer_class=TodomodelSerializer
    def get(self, request, *args, **kwargs):
        all_data = Todomodel.objects.all()
        serializer = TodomodelSerializer(all_data, many=True)
        context = {'all_data': serializer.data}
        return render(request, 'all_task.html', context)

    def post(self, request, *args, **kwargs):
        serializer = TodomodelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/todo_page/')
        return render(request, 'todo.html')




def delete_data(req, todo_id):
    if req.method == 'POST':
        todo_item = get_object_or_404(Todomodel, id=todo_id)
        todo_item.delete()
        return redirect('send-data')  
    else:
        return HttpResponse('Only POST requests are allowed')

 

def edit_todo(request, todo_id):
    todo = get_object_or_404(Todomodel, id=todo_id)

    if request.method == 'POST':
        # Process the form data (assuming you're not using a Django form)
        title = request.POST.get('title')
        description = request.POST.get('description')
        # Update the todo item
        todo.Title = title
        todo.Description = description
        todo.save()
        return redirect('todo-page')  # Redirect to the homepage or wherever appropriate

    return render(request, 'edit.html', {'todo': todo})




 