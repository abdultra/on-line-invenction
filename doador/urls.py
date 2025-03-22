from django.urls import path
from .views import (
	DoadorListView, DoadorDetailView, DoadorCreateView, DoadorUpdateView, DoadorDeleteView, doadorHome 
)

app_name = 'doador'

urlpatterns = [
	path('', doadorHome, name='doadorHome'),
	path('doadores/', DoadorListView.as_view(), name='doador_lista'),
	path('doador/<int:pk>/', DoadorDetailView.as_view(), name='doador_detalhes'),
	path('doador/novo/', DoadorCreateView.as_view(), name='doador_novo'),
	path('doador/<int:pk>/editar/', DoadorUpdateView.as_view(), name='doador_editar'),
	path('doador/<int:pk>/excluir/', DoadorDeleteView.as_view(), name='doador_excluir'),
	]