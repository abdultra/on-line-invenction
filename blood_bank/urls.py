from django.urls import path
from . import views

app_name = 'blood_bank'

urlpatterns = [
	# Doador
	path('doador/criar/', views.DoadorCreateView.as_view(), name='criar_doador'),
	path('doador/listar/', views.DoadorListView.as_view(), name='listar_doador'),
	path('doador/<int:pk>/', views.DoadorDetailView.as_view(), name='detalhes_doador'),
	path('doador/<int:pk>/atualizar/', views.DoadorUpdateView.as_view(), name='atualizar_doador'),
	path('doador/<int:pk>/excluir/', views.DoadorDeleteView.as_view(), name='excluir_doador'),

	# Doação
	path('doacao/criar/', views.DoacaoCreateView.as_view(), name='criar_doacao'),
	path('doacao/listar/', views.DoacaoListView.as_view(), name='listar_doacao'),
	path('doacao/<int:pk>/', views.DoacaoDetailView.as_view(), name='detalhes_doacao'),
	path('doacao/<int:pk>/atualizar/', views.DoacaoUpdateView.as_view(), name='atualizar_doacao'),
	path('doacao/<int:pk>/excluir/', views.DoacaoDeleteView.as_view(), name='excluir_doacao'),

	# Estoque de Sangue
	path('estoque/criar/', views.EstoqueCreateView.as_view(), name='criar_estoque'),
	path('estoque/listar/', views.EstoqueListView.as_view(), name='listar_estoque'),
	path('estoque/<int:pk>/', views.EstoqueDetailView.as_view(), name='detalhes_estoque'),
	path('estoque/<int:pk>/atualizar/', views.EstoqueUpdateView.as_view(), name='atualizar_estoque'),
	path('estoque/<int:pk>/excluir/', views.EstoqueDeleteView.as_view(), name='excluir_estoque'),
]