from django.shortcuts import render,redirect
from .models import Todo_Item


# Create your views here.

def todo(request):
    ti_list = Todo_Item.objects.all()
    return render(request, "index.html",{'ti_list':ti_list})

def add_item(request):
    item = request.POST['content']
    Todo_Item.objects.create(content=item)
    return redirect(todo)

def delete_item(request,todo_id):
    item_to_delete = Todo_Item.objects.get(id=todo_id)
    item_to_delete.delete()
    return redirect(todo)
