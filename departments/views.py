from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from departments.models import Departamento

class Department(ListView):
    model = Departamento
    fields = ['nome']

    def get_queryset(self):
        return Departamento.objects.all


class CreateDepartment(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        form.save(commit = True)
        return super(CreateDepartment, self).form_valid(form)