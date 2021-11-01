from django.shortcuts import render

def WorkOrderHome(request):
    return render(request, 'workOrder/WorkOrder.html')