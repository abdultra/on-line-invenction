from django.urls import path
from .views import(
	DoacaoListView, DoacaoDetailView, DoacaoCreateView, DoacaoUpdateView, DoacaoDeleteView
)

app_name = 'doacao'

urlpatterns = [
	path('doacoes/', DoacaoListView.as_view(), name='doacao_lista'),
	path('doacoes/<int:pk>/', DoacaoDetailView.as_view(), name='doacao_detalhes'),
	path('doacoes/novo/', DoacaoCreateView.as_view(), name='doacao_novo'),
	path('doacoes/<int:pk>/editar/', DoacaoUpdateView.as_view(), name='doacao_editar'),
	path('doacoes/<int:pk>/excluir/', DoacaoDeleteView.as_view(), name='doacao_excluir'),
	]
