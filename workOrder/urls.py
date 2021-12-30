from django.urls import path
from . import views

app_name = 'workOrder'

urlpatterns = [
    path("workOrder/", views.WorkOrderHome, name="Home_WorkOrder"),
    path("NewWorkOrder/", views.NewWorkOrder, name="New_WorkOrder"),
    path("UpdateWorkOrder/<int:id>", views.UpdateWorOrder, name="Update_WorkOrder"),
    path("DeleteWorkOrder/<int:id>", views.DeleteWorkOrder, name="Delete_WorkOrder")
]
