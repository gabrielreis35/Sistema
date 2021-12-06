from django.shortcuts import redirect, render
from produtos.forms import WorkOrderForm
from django.core.paginator import Paginator


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