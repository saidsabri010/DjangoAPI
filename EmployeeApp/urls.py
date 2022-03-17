import imp

from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from EmployeeApp.models import Departments, Employees
from EmployeeApp.views import DepartmentView, EmployeeView

urlpatterns = [
    path('department', csrf_exempt(DepartmentView.as_view())),
    path('department/<int:id>', csrf_exempt(DepartmentView.as_view())),

    path('employee', csrf_exempt(EmployeeView.as_view())),
    path('employee/<int:id>', csrf_exempt(EmployeeView.as_view()))
]
