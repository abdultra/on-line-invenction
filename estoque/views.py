from django.shortcuts import render
from .models import EstoqueSangue
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



class EstoqueSangueListView(ListView):
	model = EstoqueSangue
	template_name = "estoque/lista.html"
	context_object_name = "estoques"

class EstoqueSangueDetailView(DetailView):
	model = EstoqueSangue
	template_name = "estoque/detalhes.html"

class EstoqueSangueCreateView(CreateView):
	model = EstoqueSangue
	template_name = "estoque/formulario.html"
	fields = '__all__'
	success_url = reverse_lazy('estoque:estoque_lista')

class EstoqueSangueUpdateView(UpdateView):
	model = EstoqueSangue
	template_name = "estoque/formulario.html"
	fields = '__all__'
	success_url = reverse_lazy('estoque:estoque_lista')

class EstoqueSangueDeleteView(DeleteView):
	model = EstoqueSangue
	template_name = "estoque/excluir.html"
	success_url = reverse_lazy('estoque:estoque_lista')