#imports necessários

from django.db import models


class Produto(models.Model):
	nome = models.CharField(max_length=30)
	valor = models.DecimalField(max_digits=6, decimal_places=2)
	codigo = models.CharField(max_length = 5)
	descricao = models.TextField()

	def __str__(self):
		return self.name
		
