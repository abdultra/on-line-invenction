from django.shortcuts import render
from django.urls import reverse_lazy
from doador.models import Doador
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def doadorHome(request):
	return render(request, 'doador/home.html')
	
class DoadorListView(ListView):
	model = Doador
	template_name = "doador/lista.html"
	context_object_name = "doadores"

class DoadorDetailView(DetailView):
	model = Doador
	template_name = "doador/detalhes.html"

class DoadorCreateView(CreateView):
	model = Doador
	template_name = "doador/formulario.html"
	fields = '__all__'
	success_url = reverse_lazy('doador:doador_lista')

class DoadorUpdateView(UpdateView):
	model = Doador
	template_name = "doador/formulario.html"
	fields = '__all__'
	success_url = reverse_lazy('doador:doador_lista')

class DoadorDeleteView(DeleteView):
	model = Doador
	template_name = "doador/excluir.html"
	success_url = reverse_lazy('doador:doador_lista')