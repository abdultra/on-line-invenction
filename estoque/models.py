from django.db import models
from transfusao.models import Transfusao
from doacao.models import Doacao
from tipagem.models import TipoSanguineo  # Certifique-se de importar este modelo

class EstoqueSangue(models.Model):
	tipo_sanguineo = models.ForeignKey(TipoSanguineo, on_delete=models.PROTECT)
	quantidade_total = models.PositiveIntegerField(default=0)

	class Meta:
		verbose_name = "Estoque de Sangue"
		verbose_name_plural = "Estoques de Sangue"

	def atualizar_estoque(self):
		total_doacoes = Doacao.objects.filter(
			tipo_sanguineo=self.tipo_sanguineo
		).aggregate(total=models.Sum('quantidade'))['total'] or 0

		total_transfusoes = Transfusao.objects.filter(
			doacao__tipo_sanguineo=self.tipo_sanguineo
		).aggregate(total=models.Sum('quantidade_utilizada'))['total'] or 0

		self.quantidade_total = max(total_doacoes - total_transfusoes, 0)
		self.save()

	def __str__(self):
		return f"{self.tipo_sanguineo} - {self.quantidade_total} ml"