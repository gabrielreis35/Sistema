from django.forms import ModelForm, widgets
from .models import Departamento


class DepartmentForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nome']
