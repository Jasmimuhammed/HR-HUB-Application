from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department, Role, EmploymentHistory, Document
from .forms import EmployeeForm, DepartmentForm, RoleForm, EmploymentHistoryForm, DocumentForm

from django.contrib.auth.decorators import login_required


# Employee views
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_management/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_management/employee_detail.html', {'employee': employee})

@login_required
def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_management:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_management/employee_form.html', {'form': form})

@login_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_management:employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_management/employee_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_management:employee_list')
    return render(request, 'employee_management/employee_confirm_delete.html', {'employee': employee})

