from django.urls import path, include
from rest_framework import routers
from .views import EmployeeViewSet

routers = routers.DefaultRouter()
routers.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(routers.urls)),
    
]
