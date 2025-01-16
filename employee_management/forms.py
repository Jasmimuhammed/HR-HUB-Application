from django import forms
from .models import Employee, Department, Role, EmploymentHistory, Document

# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 
                  'date_of_birth', 'date_of_joining', 'status', 'department', 
                  'role', 'manager', 'profile_picture']
        widgets = {

        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
        'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter address'}),
        'date_of_joining': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
        'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select status'}),
        'department': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select department'}),
        'role': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select role'}),
        'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select manager'}),
        'profile_picture': forms.FileInput(attrs={'class': 'form-control-file'}),
        }


    #def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        #for field in self.fields.values():
            #field.widget.attrs['class'] = 'form-control'

        #if self.instance.department:
            #self.fields['manager'].queryset = Employee.objects.filter(department=self.instance.department).exclude(pk=self.instance.pk)
        #else:
            #self.fields['manager'].queryset = Employee.objects.none()

            
    #to ensure email is unique:validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Employee.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
    #An employee cannot be their own manager
    def clean_manager(self):
        manager = self.cleaned_data.get('manager')
        if manager and manager == self.instance:
            raise forms.ValidationError("An employee cannot be their own manager.")
        return manager
    #to ensure phone number is unique:validation
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and Employee.objects.filter(phone_number=phone_number).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This phone number is already associated with an existing employee.")
        return phone_number
# Department Form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']

# Role Form
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['title', 'description']

# Employment History Form
class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = ['employee', 'effective_date', 'previous_role', 'new_role', 'previous_department', 
                  'new_department', 'previous_salary', 'new_salary', 'reason_for_change']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.employee:
            self.fields['previous_role'].initial = self.instance.employee.role
            self.fields['previous_department'].initial = self.instance.employee.department

# Document Form
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['employee', 'document_name', 'file_path']
    
    def clean_file_path(self):
        file = self.cleaned_data.get('file_path')
        if file and file.size > 5 * 1024 * 1024:  # Example: 5MB limit
            raise forms.ValidationError("Document size exceeds 5MB.")
        return file