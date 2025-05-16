from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Todo
from .forms import TodoCreateForm


# Listing all Todos.
def home(request):
    query = request.GET.get('q')
    if query:
        todo_list = Todo.objects.filter(
            Q(name__icontains = query)
        )
    else:
        todo_list = Todo.objects.all()

    return render(request,'Todo/home.html',{'todos':todo_list})


# Creating New Todo
def create_todo(request):
    if request.method == 'POST':
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Todo Has Been Created.')
            return redirect('home')
    else:
        form = TodoCreateForm()

    return render(request, 'Todo/create_todo.html', {'form': form})

        

# edit todo 
def edit_todo(request,pk):
    todo = get_object_or_404(Todo,pk = pk)
    if request.method == 'POST':
        form = TodoCreateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Todo Has Been Updated.')
            return redirect('home')
    else:
        form = TodoCreateForm(instance=todo)

    return render(request, 'Todo/edit_todo.html', {'form': form})
