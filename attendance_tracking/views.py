from django.shortcuts import render, get_object_or_404
from .models import Attendance
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import date,time
from django.contrib import messages
from django.shortcuts import redirect
from datetime import timedelta

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        # Check if the request is to mark attendance
        status = request.POST.get('status')
        date = request.POST.get('date')  # Assuming you get the date from the form
        check_in_time = request.POST.get('check_in_time')
        check_out_time = request.POST.get('check_out_time')

        # Find or create the attendance record for the current user and date
        attendance, created = Attendance.objects.get_or_create(employee=request.user, date=date)

        if status:
            # Save the status when Mark Attendance button is clicked
            attendance.status = status
            attendance.save()

        if check_in_time and check_out_time:
            # Calculate total hours if both check-in and check-out times are provided
            check_in = timedelta(hours=int(check_in_time.split(':')[0]), minutes=int(check_in_time.split(':')[1]))
            check_out = timedelta(hours=int(check_out_time.split(':')[0]), minutes=int(check_out_time.split(':')[1]))

            # Calculate total hours worked
            total_worked = (check_out - check_in).total_seconds() / 3600  # Convert to hours

            # Save the total hours to the Attendance record
            attendance.total_hours = round(total_worked, 2)
            attendance.save()

        return redirect('attendance_tracking:mark_attendance')  # Redirect to a page showing attendance details

    return render(request, 'attendance_tracking/mark_attendance.html')

@login_required
def attendance_report(request):
    attendance_records = Attendance.objects.filter(employee=request.user)
    return render(request, 'attendance_tracking/attendance_report.html', {'records': attendance_records})
