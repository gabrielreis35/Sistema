from django.urls import path
from . import views

app_name = 'workOrder'

urlpatterns = [
    path("workOrder/", views.WorkOrderHome, name="Home_WorkOrder")
]
