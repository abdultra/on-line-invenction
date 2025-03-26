from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import (
	CreateView, ListView, DetailView, UpdateView, DeleteView
)
from .models import Doador, Doacao, EstoqueSangue

# -------------------- DOADOR --------------------
class DoadorCreateView(CreateView):
	model = Doador
	template_name = 'criar.html'
	fields = '__all__'
	success_url = reverse_lazy('doador:listar')

class DoadorListView(ListView):
	model = Doador
	template_name = 'lista.html'
	context_object_name = 'doadores'

class DoadorDetailView(DetailView):
	model = Doador
	template_name = 'detalhes.html'
	context_object_name = 'doador'

class DoadorUpdateView(UpdateView):
	model = Doador
	template_name = 'atualizar.html'
	fields = '__all__'
	success_url = reverse_lazy('doador:listar')

class DoadorDeleteView(DeleteView):
	model = Doador
	template_name = 'excluir.html'
	success_url = reverse_lazy('doador:listar')

# -------------------- DOAÇÃO ----------------------------
class DoacaoCreateView(CreateView):
	model = Doacao
	template_name = 'criar.html'
	fields = '__all__'
	success_url = reverse_lazy('doacao:listar')

class DoacaoListView(ListView):
	model = Doacao
	template_name = 'lista.html'
	context_object_name = 'doacoes'

class DoacaoDetailView(DetailView):
	model = Doacao
	template_name = 'detalhes.html'
	context_object_name = 'doacao'

class DoacaoUpdateView(UpdateView):
	model = Doacao
	template_name = 'atualizar.html'
	fields = '__all__'
	success_url = reverse_lazy('doacao:listar')

class DoacaoDeleteView(DeleteView):
	model = Doacao
	template_name = 'excluir.html'
	success_url = reverse_lazy('doacao:listar')

# ----------------- ESTOQUE DE SANGUE --------------------
class EstoqueCreateView(CreateView):
	model = EstoqueSangue
	template_name = 'criar.html'
	fields = '__all__'
	success_url = reverse_lazy('estoque:listar')

class EstoqueListView(ListView):
	model = EstoqueSangue
	template_name = 'lista.html'
	context_object_name = 'estoques'

class EstoqueDetailView(DetailView):
	model = EstoqueSangue
	template_name = 'detalhes.html'
	context_object_name = 'estoque'

class EstoqueUpdateView(UpdateView):
	model = EstoqueSangue
	template_name = 'atualizar.html'
	fields = '__all__'
	success_url = reverse_lazy('estoque:listar')

class EstoqueDeleteView(DeleteView):
	model = EstoqueSangue
	template_name = 'excluir.html'
	success_url = reverse_lazy('estoque:listar')