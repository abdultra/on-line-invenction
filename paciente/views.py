from django.shortcuts import render
from django.db import models

class PacienteListView(ListView):
    model = Paciente
    template_name = 'paciente/lista.html'
    context_object_name = 'pacientes'

class PacienteDetailView(DetailView):
    model = Paciente
    template_name = 'paciente/detalhes.html'

class PacienteCreateView(CreateView):
    model = Paciente
    fields = "__all__"
    template_name = 'paciente/formulario.html'
    success_url = reverse_lazy('paciente_lista')

class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = "__all__"
    template_name = 'paciente/formulario.html'
    success_url = reverse_lazy('paciente_lista')

class PacienteDeleteView(DeleteView):
    model = Paciente
    template_name = 'paciente/excluir.html'
    success_url = reverse_lazy('paciente_lista')