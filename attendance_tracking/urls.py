from django.urls import path
from . import views

app_name = 'attendance_tracking'
urlpatterns = [
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('report/', views.attendance_report, name='attendance_report'),
]
