from django.shortcuts import render
from .models import Doacao
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class DoacaoListView(ListView):
	model = Doacao
	template_name = "doacao/lista.html"
	context_object_name = "doacoes"

class DoacaoDetailView(DetailView):
	model = Doacao
	template_name = "doacao/detalhes.html"

class DoacaoCreateView(CreateView):
	model = Doacao
	template_name = "doacao/formulario.html"
	fields = '__all__'
	success_url = reverse_lazy('doacao:doacao_lista')

class DoacaoUpdateView(UpdateView):
	model = Doacao
	template_name = "doacao/formulario.html"
	fields = '__all__'
	success_url = reverse_lazy('doacao:doacao_lista')

class DoacaoDeleteView(DeleteView):
	model = Doacao
	template_name = "doacao/excluir.html"
	success_url = reverse_lazy('doacao:doacao_lista')