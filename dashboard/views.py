from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from employee_management.models import Employee




@login_required
def dashboard(request):
    total = Employee.objects.count()
    employees = Employee.objects.all()

    # Filtering logic
    name_query = request.GET.get('name', '').strip()
    department_query = request.GET.get('department', '').strip()
    role_query = request.GET.get('role', '').strip()

    if name_query:
        employees = employees.filter(first_name__icontains=name_query)
    if department_query:
        employees = employees.filter(department__name__icontains=department_query)
    if role_query:
        employees = employees.filter(role__title__icontains=role_query)
    
    return render(request, 'dashboard/dashboard.html', {'total_employees': total,'employees': employees})

def sidebar(request):
    
    return render(request, 'sidebar.html')

def topbar(request):
    
    return render(request, 'topbar.html')

def footer(request):
    
    return render(request, 'footer.html')


