#imports necessários

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Produto
from .forms import ProdutoForm

# views da app Prodotus 

@login_required  # requerimento de login para acessar as views

def novo_produto(request):
	form = ProdutoForm(request.POST or None, request.FILES or None)

	if  form.is_valid():
		
		form.save()
		return redirect('lista-produto')

	return render(request,'novo_produto.html',{'form': form})

@login_required
def lista_produto(request):
	produto = Produto.objects.all()
	return render(request,'lista_produto.html',{'produto':produto})

@login_required
def update(request,id):
	produto = get_object_or_404(Produto,pk=id)
	form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

	if form.is_valid():
		form.save()
		return redirect('lista-produto')

	return render(request,'novo_produto.html',{'form': form})
	

@login_required

def delete(request,id):
	produto = get_object_or_404(Produto,pk=id)
	form = ProdutoForm(request.POST or None, request.FILES or None, instance=produto)

	if request.method == 'POST':
		produto.delete()
		return redirect('lista-produto')
	return render(request,'produto_delete.html',{'form':form})
	

