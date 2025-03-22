from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
from paciente.models import Paciente  # Única dependência externa

# Modelo TipoSanguineo
class TipoSanguineo(models.Model):
	TIPO_CHOICES = [
		('A+', 'A+'), ('A-', 'A-'),
		('B+', 'B+'), ('B-', 'B-'),
		('AB+', 'AB+'), ('AB-', 'AB-'),
		('O+', 'O+'), ('O-', 'O-'),
	]
	tipo = models.CharField(max_length=3, choices=TIPO_CHOICES, unique=True)

	class Meta:
		verbose_name = "Tipo Sanguíneo"
		verbose_name_plural = "Tipos Sanguíneos"

	def __str__(self):
		return self.tipo


# Modelo Doador
class Doador(models.Model):
	numero_doador = models.CharField(max_length=255, unique=True)
	nome_completo = models.CharField(max_length=255)
	tipo_sanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.PROTECT)
	telefone = models.CharField(max_length=9)
	data_nascimento = models.DateField()

	class Meta:
		verbose_name = "Doador"
		verbose_name_plural = "Doadores"

	def __str__(self):
		return f"{self.nome_completo} - {self.tipo_sanguineo}"

	@property
	def idade(self):
		return relativedelta(date.today(), self.data_nascimento).years

	def clean(self):
		if self.data_nascimento:
			if self.data_nascimento > date.today():
				raise ValidationError({"data_nascimento": "A data de nascimento não pode ser no futuro."})
			if self.data_nascimento < date.today().replace(year=date.today().year - 120):
				raise ValidationError({"data_nascimento": "A data de nascimento é muito antiga."})
		else:
			raise ValidationError({"data_nascimento": "O campo de data de nascimento não pode ser vazio."})


# Modelo Doacao
class Doacao(models.Model):
	numero_saco = models.CharField(max_length=255, unique_for_year=True)
	doador = models.ForeignKey(Doador, on_delete=models.CASCADE)
	quantidade = models.PositiveIntegerField()
	data = models.DateField(auto_now_add=True)
	foi_adicionado_ao_estoque = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Doação"
		verbose_name_plural = "Doações"
		ordering = ['-data']

	def __str__(self):
		return f"Doação {self.numero_saco} - {self.doador.nome_completo} ({self.data})"

	def save(self, *args, **kwargs):
		self.clean()

		if not self.foi_adicionado_ao_estoque:
			estoque, _ = EstoqueSangue.objects.get_or_create(
				tipo_sanguineo=self.doador.tipo_sanguineo
			)
			estoque.quantidade_total += self.quantidade
			estoque.save()

			self.foi_adicionado_ao_estoque = True

		super().save(*args, **kwargs)

	def clean(self):
		if self.quantidade < 350:
			raise ValidationError("O volume mínimo permitido para doação é 350 ml.")
		if self.quantidade > 500:
			raise ValidationError("O volume máximo permitido para doação é 500 ml.")


# Modelo EstoqueSangue
class EstoqueSangue(models.Model):
	tipo_sanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.PROTECT)
	quantidade_total = models.PositiveIntegerField(default=0)

	class Meta:
		verbose_name = "Estoque de Sangue"
		verbose_name_plural = "Estoques de Sangue"

	def atualizar_estoque(self):
		total_doacoes = Doacao.objects.filter(
			doador__tipo_sanguineo=self.tipo_sanguineo
		).aggregate(total=models.Sum('quantidade'))['total'] or 0

		total_transfusoes = Transfusao.objects.filter(
			paciente__tipo_sanguineo=self.tipo_sanguineo
		).aggregate(total=models.Sum('quantidade_utilizada'))['total'] or 0

		self.quantidade_total = max(total_doacoes - total_transfusoes, 0)
		self.save()

	def __str__(self):
		return f"{self.tipo_sanguineo} - {self.quantidade_total} ml"