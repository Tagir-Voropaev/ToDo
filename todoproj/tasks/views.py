from django.shortcuts import render, redirect
from .models import Task_model
from .forms import Task_modelForm



def tasks(request):
    error = ''
    if request.method == 'POST':
        form = Task_modelForm(request.POST)
        if form.is_valid():
            form.save()
            error = ''
            return redirect('tasks')
        else:
            error = 'Некорректные данные'
    tasks = Task_model.objects.all()
    form = Task_modelForm()

    return render(request, 'tasks/tasks.html', {'tasks': tasks, 'form' : form, 'error' : error})

