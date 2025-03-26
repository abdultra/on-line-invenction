from django.urls import path
from .views import (
	PacienteListView,
	PacienteDetailView,
	PacienteCreateView,
	PacienteUpdateView,
	PacienteDeleteView
)

app_name = 'paciente'

urlpatterns = [
	path('', PacienteListView.as_view(), name='paciente_lista'),
	path('<int:pk>/', PacienteDetailView.as_view(), name='paciente_detalhes'),
	path('criar/', PacienteCreateView.as_view(), name='paciente_criar'),
	path('editar/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_editar'),
	path('excluir/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_excluir'),
]