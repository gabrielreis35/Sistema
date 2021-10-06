from django.urls import path
from .views import Department, CreateDepartment

app_name = 'departments'

urlpatterns = [
    path('', Department.as_view(template_name= 'departments/departments.html'), name = 'Home_Departments'),
    path('newDepartment', CreateDepartment.as_view(template_name = 'departments/NewDepartment.html'), name = 'New_Department'),
]
