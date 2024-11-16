from .models import Task_model
from django.forms import ModelForm, TextInput, TimeInput, DateInput

class Task_modelForm(ModelForm):
    class Meta:
        model = Task_model
        fields = ['title_task', 'date_task', 'time_task']
        widgets = {
            'title_task': TextInput(attrs={
                'class' : 'task-add-task task-add-input',
                'placeholder' : 'Введите задачу',
            }),
            'date_task': DateInput(attrs={
                'class' : 'task-add-date task-add-input',
                'placeholder' : 'Введите дату',
                'type' : 'date'
            }),
            'time_task': TimeInput(format='%H:%M', attrs={
                'class' : 'task-add-time task-add-input',
                'placeholder' : 'Введите время',
                'type' : 'time'
            })
        }