from django.db import models

# Create your models here.

class Produtos():
    def __init__(self, id, nome, preco, validade) -> None:
        self.id = id
        self.nome = nome
        self.preco = preco
        self.validade = validade

