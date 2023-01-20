#!/usr/bin/env python3
"""Cadastro de produto"""
__version__ = "0.1.0"

import pprint

# produto_nome = "Caneta"
# produto_cor1 = "azul"
# produto_cor2 = "branco"
# produto_preco = 3.23
# produto_dimensao_altura = 12.1
# produto_dimensao_largura = 0.8
# produto_em_estoque = True
# produto_codigo = 45678
# produto_codebar = None

# Nós podemos substituir várias variáveis de um mesmo produto por um dicionário

produto = {
    "nome": "Caneta",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

# compra = ("Bruno", produto["nome"], 3)
# Da mesma forma as demais variáveis do programa podem fazer uso das características dos dicionários.
# O trecho acima pode ser reescrito da seguinte forma:

cliente = {
    "nome": "Bruno"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

# Podemos fazer uso da biblioteca pprint para imprimir as saídas de dicionários de uma forma mais amigável. 

pprint.pprint(compra)

# total_compra = compra[2] * produto["preco"]
# 
# print (
#     f"O cliente {compra[0]} comprou {compra[1]}"
#     f" e pagou o total de {total_compra}"
# )

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print (
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)