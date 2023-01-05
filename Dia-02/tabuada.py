#!/usr/bin/env python
"""Imprime a tabuada do 1 ao 10
---Tabuada do 1---
1 x 1 = 1
1 x 2 = 2
...
#####
---Tabuada do 2---
1 x 2 = 2 
2 x 2 = 4
...
#####
"""

__version__ = "0.1.0"
__author__ = "Ivo Rafael"

# O objeto range apresenta uma sequência de forma não inclusive, portanto é 
# necessário informar um número a mais ao final. No nosso exemplo para irmos 
# de 1 a 10 é necessário informar os argumentos como (1, 11). Para termos o
# retorno como lista é necessário efetuar um cast, conforme apresentado abaixo.

numeros = list(range(1,11))

# numeros = [1,2,3,4,5,6,7,8,9,10]

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}\n"))
    print("#" * 18)
