"""
3) Desenvolver um programa que apresente os quadrados dos números inteiros de 15 a 200.
"""
import math

contador = 15

while contador <= 200:
    quadrado = math.pow(contador, 2)
    print(f"O quadrado de {contador} é {quadrado:.0f}")
    contador = contador + 1
