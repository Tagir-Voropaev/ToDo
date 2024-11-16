from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('timetable', views.timetable, name='timetable'),
    path('scripts', views.scripts, name='scripts'),
    path('payment', views.payment, name='payment'),
]
