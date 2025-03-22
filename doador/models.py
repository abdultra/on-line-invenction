from django.db import models
from tipagem.models import TipoSanguineo
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from genero.models import Genero
from dateutil.relativedelta import relativedelta

class Doador(models.Model):
	numero_doador = models.CharField(max_length=255, unique=True)
	
	nome_completo = models.CharField(max_length=255)
	tipo_sanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.PROTECT)
	genero = models.ForeignKey(Genero, on_delete = models.CASCADE)
	telefone = models.CharField(max_length=9)
	data_nascimento = models.DateField()
	
	class Meta:
		verbose_name = "Doador"
		verbose_name_plural = "Doadores"

	def __str__(self):
		return f"{self.nome_completo} - {self.tipo_sanguineo}"
		
	# Propriedade para calcular a idade
	@property
	def idade(self):
		return relativedelta(date.today(), self.data_nascimento).years

	# Método clean para validação do modelo
	def clean(self):
		# Verifica se o campo nascimento não é None
		if self.data_nascimento is not None:
			# Verifica se a data de nascimento é no futuro
			if self.data_nascimento > date.today():
				raise ValidationError({"nascimento": "A data de nascimento não pode ser no futuro."})

			# Verifica se a data de nascimento é mais antiga do que 120 anos
			if self.data_nascimento < date.today().replace(year=date.today().year - 120):
				raise ValidationError({"nascimento": "A data de nascimento é muito antiga. Verifique se está correta."})
		else:
			raise ValidationError({"nascimento": "O campo de data de nascimento não pode ser vazio."})