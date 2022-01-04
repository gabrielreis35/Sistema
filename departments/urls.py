from django.urls import path
from .views import CreateDepartment, HomeDepartment, DeleteDepartment

app_name = 'departments'

urlpatterns = [
    path('', HomeDepartment, name = 'Home_Departments'),
    path('newDepartment', CreateDepartment, name = 'New_Department'),
    path("deleteDepartment/<int:id>", DeleteDepartment, name="Delete_Department")
]
