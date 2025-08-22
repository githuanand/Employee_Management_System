from django.contrib import admin
from .models import Employee, Department


# Inline Employee display inside Department
class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1


# Department Admin
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)
    inlines = [EmployeeInline]


# Employee Admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "role", "department", "date_joined")
    list_filter = ("department", "role")
    search_fields = ("name", "email", "role")
    ordering = ("-date_joined",)
