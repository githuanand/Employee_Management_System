from django import forms
from .models import Employee, Department


# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "email", "phone", "role", "department"]


# Department Form
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name", "description"]
