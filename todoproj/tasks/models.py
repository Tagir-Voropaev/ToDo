from django.db import models
from datetime import datetime

class Task_model(models.Model):
    title_task = models.CharField('Заголовок', max_length=100, default='', help_text='Введите задачу')
    date_task = models.DateField(default=datetime.now)
    time_task = models.TimeField(default=datetime.now)

    def __str__(self):
        return '{}'.format(self.title_task)
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'