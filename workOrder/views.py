from django.shortcuts import redirect, render
from produtos.forms import WorkOrderForm

from workOrder.models import OrdemServico

def WorkOrderHome(request):
    workOrders = OrdemServico.objects.all()
    return render(request, 'workOrder/WorkOrder.html', {'workOrders' : workOrders})

def NewWorkOrder(request):
    workOrderForm = WorkOrderForm()
    if request.method == 'POST':
        workOrderForm = WorkOrderForm(request.POST or None)
        if workOrderForm.is_valid():
            workOrderForm.save()
            return redirect('/workOrder/workOrder')
    else:
        workOrderForm = WorkOrderForm()
    return render(request, 'workOrder/NewWorkOrder.html', {'workOrderForm': workOrderForm})