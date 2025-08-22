from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm


# Dashboard
def home(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    emp_count = employees.count()
    dept_count = departments.count()
    recent_employees = employees.order_by('-date_joined')[:5]

    return render(request, "hr/home.html", {
        "employees": employees,
        "departments": departments,
        "emp_count": emp_count,
        "dept_count": dept_count,
        "recent_employees": recent_employees
    })


# Employee List
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, "hr/employee_list.html", {"employees": employees})


# Add Employee
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm()
    return render(request, "hr/add_employee.html", {"form": form})


# Edit Employee
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employee_list")
    else:
        form = EmployeeForm(instance=employee)
    return render(request, "hr/edit_employee.html", {"form": form})


# Delete Employee
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect("employee_list")


# Department List
def department_list(request):
    departments = Department.objects.all()
    return render(request, "hr/department_list.html", {"departments": departments})


# Add Department
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm()
    return render(request, "hr/add_department.html", {"form": form})


# Edit Department
def edit_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm(instance=department)
    return render(request, "hr/edit_department.html", {"form": form})


# Delete Department
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    department.delete()
    return redirect("department_list")


# Search Employees
def search_employees(request):
    query = request.GET.get('q', '')
    employees = Employee.objects.filter(name__icontains=query)
    return render(request, "hr/employee_list.html", {"employees": employees, "query": query})


# Search Departments
def search_departments(request):
    query = request.GET.get('q', '')
    departments = Department.objects.filter(name__icontains=query)
    return render(request, "hr/department_list.html", {"departments": departments, "query": query})


# View Employee Details
def view_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "hr/view_employee.html", {"employee": employee})


# View Department Details
def view_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    employees = Employee.objects.filter(department=department)
    return render(request, "hr/view_department.html", {"department": department, "employees": employees})
