from django.db import models
from datetime import date
from django.core.exceptions import ValidationError


class Paciente(models.Model):
	class Genero(models.TextChoices):
		MASCULINO = "Masculino", "Masculino"
		FEMININO = "Feminino", "Feminino"

	class Proveniencia(models.TextChoices):
		SUR = 'SUR', 'Servico de Urgencia de Reanimacao'
		PED = 'PED', 'Pediatria'
		CIR = 'CIR', 'Cirurgia'
		GIN = 'GIN', 'Ginecologia'
		OBST = 'OBST', 'Obstetricia'
		UROL = 'UROL', 'Urologia'
		MED_I = 'MED_I', 'Medicina Homem'
		MED_II = 'MED_II', 'Medicina Mulher'
		OFT = 'OFT', 'Oftalmologia'
		C_EXT = 'C.EXT', 'Consulta Externa'
		BS = 'BS', 'Banco de Socorros'
		AMB = 'AMB', 'Ambulatorio'
	
	nome = models.CharField(max_length=255, db_index=True)
	nascimento = models.DateField()
	genero = models.CharField(max_length=10, choices=Genero.choices)
	telefone = models.CharField(max_length = 9, unique=True)
	nacionalidade = CountryField(blank=False, default="MZ")
	residencia = models.CharField(max_length=255, blank=True)
	proveniencia = models.CharField(choices=Proveniencia.choices, max_length=255, blank=True)
	historico_medico = models.TextField(blank=True, null=True)

	class Meta:
		verbose_name = "Paciente"
		verbose_name_plural = "Pacientes"

	def __str__(self):
		return f"{self.nome} ({self.id})"

	@property
	def idade(self):
		hoje = date.today()
		return hoje.year - self.nascimento.year - ((hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day))

	def clean(self):
		if self.nascimento > date.today():
			raise ValidationError("A data de nascimento não pode ser no futuro.")