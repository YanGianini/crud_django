from django.shortcuts import redirect, render, HttpResponseRedirect
from crud.models import Produtos
from crud.forms.forms import ProdutoForm

produto1 = Produtos(1, "Água", 2.00, "15/10/30")
produto2 = Produtos(2, "Torta alemã", 6.00, "15/03/2022")

produtos = [produto1, produto2]

def index(request):
    return render(request, "index.html", context={'produtos': produtos})

def cadastro(request):
    produto_form = ProdutoForm()
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            id = len(produtos) + 1
            produto = Produtos(id,
                form.cleaned_data['nome'],
                form.cleaned_data['preco'],
                form.cleaned_data['validade']
            )
            produtos.append(produto)
            return HttpResponseRedirect('/home/')
        return render(request, "cadastro.html", context={'produto_form':produto_form})

    
    return render(request, "cadastro.html", context={'produto_form':produto_form})

