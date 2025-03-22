from django.db import models
from doador.models import Doador

class Doacao(models.Model):
	numero_saco = models.CharField(
		max_length=255, unique=True, verbose_name="Número do Saco", help_text="Número de identificação único para cada bolsa de sangue."
		)

	doador = models.ForeignKey(
		Doador, on_delete=models.CASCADE, verbose_name="Doador", help_text="Selecione o doador responsável por esta doação."
		)

	quantidade = models.PositiveIntegerField(
		verbose_name="Quantidade (ml)", help_text="Inserir o volume da doação em mililitros. Mínimo 350 ml."
		)

	data = models.DateField(auto_now_add=True, verbose_name="Data da Doação"
	)

	foi_adicionado_ao_estoque = models.BooleanField(
		default=False,
		verbose_name="Adicionado ao Estoque",
		help_text="Indica se essa doação já foi integrada ao estoque."
		)

	class Meta:
		verbose_name = "Doação"
		verbose_name_plural = "Doações"
		ordering = ['-data']

	def __str__(self):
		return f"Doação {self.numero_saco} - {self.doador.nome} ({self.data})"

	def save(self, *args, **kwargs):
		"""
		Sobrescreve o método save para validar e controlar integração com estoque.
		"""
		
		self.clean()

		# Integração com estoque
		if not self.foi_adicionado_ao_estoque:
			from estoque.models import EstoqueSangue
			# Importação localizada para evitar problemas de importação circular
			estoque, _ = EstoqueSangue.objects.get_or_create(
				tipo_sanguineo=self.doador.tipo_sanguineo
				)
			estoque.quantidade_total += self.quantidadeestoque.save()

			self.foi_adicionado_ao_estoque = True  # Marca a doação como contabilizada

		super().save(*args, **kwargs)

	def clean(self):
		"""
		Validações personalizadas:
		- Volume mínimo permitido: 350 ml
		- Volume máximo permitido: 500 ml
		"""
		if self.quantidade < 350:
			raise ValidationError("O volume mínimo permitido para doação é 350 ml.")
		if self.quantidade > 500:
			raise ValidationError("O volume máximo permitido para doação é 500 ml.")