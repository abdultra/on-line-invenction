from django.urls import path
from .views import(
	EstoqueSangueListView, EstoqueSangueDetailView, EstoqueSangueCreateView, EstoqueSangueUpdateView, EstoqueSangueDeleteView
)

app_name = 'estoque'

urlpatterns = [
	path('estoques/', EstoqueSangueListView.as_view(), name='estoque_lista'),
	path('estoques/<int:pk>/', EstoqueSangueDetailView.as_view(), name='estoque_detalhes'),
	path('estoques/novo/', EstoqueSangueCreateView.as_view(), name='estoque_novo'),
	path('estoques/<int:pk>/editar/', EstoqueSangueUpdateView.as_view(), name='estoque_editar'),
	path('estoques/<int:pk>/excluir/', EstoqueSangueDeleteView.as_view(), name='estoque_excluir'),
	]