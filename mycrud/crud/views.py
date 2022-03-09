from django.shortcuts import render
from crud.models import Produtos

produto1 = Produtos("Água", 2.00, "15/10/30")
produto2 = Produtos("Torta alemã", 6.00, "15/03/2022")

produtos = [produto1, produto2]

def index(request):
    return render(request, "index.html", context={'produtos': produtos})

