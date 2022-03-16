from functools import partial
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView


from EmployeeApp.models import Employees, Departments
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
# Create your views here.

# for post : http://127.0.0.1:8000/employee/department/
# for get : http://127.0.0.1:8000/employee/department/


class DepartmentView(APIView):
    def post(self, request):
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('added succussfuly !', safe=False)
        return JsonResponse('failed to Add !', safe=False)

    def get(self, request, id=None):
        if id:
            department = Departments.objects.get(DepartmentId=id)
            department_serializer = DepartmentSerializer(
                department, data=request.data, partial=True)
            if department_serializer.is_valid():
                return JsonResponse(department_serializer.data, safe=False)
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    def put(self, request, id=None):
        department = Departments.objects.get(DepartmentId=id)
        department_serialzer = DepartmentSerializer(
            department, data=request.data, partial=True)
        if department_serialzer.is_valid():
            department_serialzer.save()
            return JsonResponse('Updated successfuly !', safe=False)
        return JsonResponse('Failed to Update !', safe=False)

    def delete(self, request, id=0):
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse('Deleted succussfuly ! ', safe=False)
