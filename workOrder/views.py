from django.shortcuts import get_object_or_404, redirect, render
from produtos.forms import WorkOrderForm
from django.core.paginator import Paginator
from workOrder.forms import ProductforWorkOrderForm

from workOrder.models import OrdemServico

def WorkOrderHome(request):
    workOrdersList = OrdemServico.objects.all().order_by('-dateCriacao')
    
    paginator = Paginator(workOrdersList, 10)
    page = request.GET.get('page')
    workOrders = paginator.get_page(page)
    context = {
        'workOrders' : workOrders
    }
    return render(request, 'workOrder/WorkOrder.html', context)

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

def UpdateWorOrder(request, id):
    workOrder = get_object_or_404(OrdemServico, id = id)
    updateWorkOrder = ProductforWorkOrderForm(instance = workOrder)
    if request.method == 'POST':
        updateWorkOrder = ProductforWorkOrderForm(request.POST or None, instance=workOrder)
        if updateWorkOrder.is_valid():
            updateWorkOrder.save()
            return redirect('../')
        else:
            context = {
                'workOrder': workOrder,
                'updateWorkOrder': updateWorkOrder
            }
    else:    
        context = {
            'workOrder': workOrder,
            'updateWorkOrder': updateWorkOrder
        }
        return render(request, 'workOrder/UpdateWorkOrder.html', context)
    
def DeleteWorkOrder(request, id):
    workOrder = get_object_or_404(OrdemServico, id = id)
    if request.method == 'POST':
        workOrder.delete()
        return redirect('../')
    context = {'workOrder': workOrder}
    return render(request, 'workOrder/DeleteWorkOrder.html', context) 