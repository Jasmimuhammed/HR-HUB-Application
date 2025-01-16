from django.db import models

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Role Model
class Role(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Employee Model
class Employee(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Probation', 'Probation'),
        ('Terminated', 'Terminated'),
        ('Retired', 'Retired'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(null=True, blank=True) 
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='employees')
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    #This method overrides the default save() method in Django models,
    # allowing you to add custom validation or behavior before saving an instance to the database
    #def save(self, *args, **kwargs):
        #if self.manager == self:
            #raise ValueError("An employee cannot be their own manager.")
        #super().save(*args, **kwargs)

# Employment History Model
class EmploymentHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='history')
    change_date = models.DateTimeField(auto_now_add=True)
    effective_date = models.DateField(blank=True, null=True)
    previous_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='previous_role')
    new_role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='new_role')
    previous_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='previous_department')
    new_department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='new_department')
    previous_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reason_for_change = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"History of {self.employee}"

# Document Model
class Document(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='documents')
    document_name = models.CharField(max_length=100)
    file_path = models.FileField(upload_to='employee_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document_name

    def delete(self, *args, **kwargs):
        if self.file_path:
            self.file_path.delete(save=False)
        super().delete(*args, **kwargs)