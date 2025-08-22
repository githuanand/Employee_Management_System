from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # Employees
    path('employees/', views.employee_list, name="employee_list"),
    path('employees/add/', views.add_employee, name="add_employee"),
    path('employees/edit/<int:pk>/', views.edit_employee, name="edit_employee"),
    path('employees/delete/<int:pk>/', views.delete_employee, name="delete_employee"),
    path('employees/view/<int:pk>/', views.view_employee, name="view_employee"),
    path('employees/search/', views.search_employees, name="search_employees"),

    # Departments
    path('departments/', views.department_list, name="department_list"),
    path('departments/add/', views.add_department, name="add_department"),
    path('departments/edit/<int:pk>/', views.edit_department, name="edit_department"),
    path('departments/delete/<int:pk>/', views.delete_department, name="delete_department"),
    path('departments/view/<int:pk>/', views.view_department, name="view_department"),
    path('departments/search/', views.search_departments, name="search_departments"),
]
