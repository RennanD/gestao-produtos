#imports necessários
from django.forms import ModelForm
from .models import Produto

#forms django

class ProdutoForm(ModelForm):
	

	class Meta:
		model = Produto
		fields = ['nome', 'valor', 'codigo', 'descricao']