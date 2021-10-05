from django.urls import path
from django.views.generic.base import TemplateView

from main.views import Home
from .views import Department, CreateDepartment


urlpatterns = [
    path('', Department.as_view(template_name= 'departments/departments.html'), name = 'Home_Departments'),
    path('newDepartment', CreateDepartment.as_view(template_name = 'departments/NewDepartment.html'), name = 'New_Department'),
]
