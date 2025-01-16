from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from datetime import date,time

def validate_time_format(value):
    if value and not isinstance(value, time):
        raise ValidationError('Time must be in HH:MM[:ss[.uuuuuu]] format.')

class Attendance(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True) 
    status = models.CharField(max_length=20)
    #check_in_time = models.TimeField(null=True, blank=True, validators=[validate_time_format])
    #check_out_time = models.TimeField(null=True, blank=True, validators=[validate_time_format])
    total_hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.employee} - {self.date} - {self.status} - {self.total_hours}'
