"""
14) Desenvolver um programa que calcule o fatorial do número 5, ou seja, 5!. Desta forma, temos que 5! = 5 . 4 . 3 .
2 . 1 ou 5! = 1 . 2 . 3 . 4 . 5, equivalente a 120.
"""

contador = 5

ant = 1

while contador > 0:
    ant = contador * ant
    contador = contador - 1

print(ant)