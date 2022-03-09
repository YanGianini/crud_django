from django.db import models

# Create your models here.

class Produtos():
    def __init__(self, nome, preco, validade) -> None:
        self.nome = nome
        self.preco = preco
        self.validade = validade


