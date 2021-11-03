from django.forms import ModelForm
from produtos.models import Produto
from workOrder.models import OrdemServico

class WorkOrderForm(ModelForm):
    class Meta:
        model = OrdemServico
        fields = [
            'OS'
        ]
        
        labels = {
            'OS': ('Ordem de Serviço')
        }

class ProductforWorkOrderForm(ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome'
        ]
        labels = {
            'nome': ('Produto Relacionado')
        }