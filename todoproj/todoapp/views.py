from django.shortcuts import render

def home(request):
    return render(request, ('todoapp/home.html'))

def timetable(request):
    return render(request, ('todoapp/timetable.html'))


def scripts(request):
    return render(request, ('todoapp/scripts.html'))


def payment(request):
    return render(request, ('todoapp/payment.html'))




