from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Employee
from .serializers import EmployeeSerializer

class EmployeePagination(PageNumberPagination):
    page_size = 10

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['department', 'role']