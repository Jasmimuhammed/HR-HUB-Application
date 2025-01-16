from django.contrib import admin
from .models import Employee, Department, Role, EmploymentHistory, Document

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'role', 'status')
    search_fields = ('first_name', 'last_name', 'email', 'department__name', 'role__title')
    list_filter = ('status', 'department', 'role')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(EmploymentHistory)
class EmploymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'change_date', 'previous_role', 'new_role', 'effective_date')


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('employee', 'document_name', 'uploaded_at')
