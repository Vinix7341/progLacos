"""
10) Desenvolver um programa que apresente as potências de 3 variando de 0 a 15. Deve ser considerado que
qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. A apresentação deve observar a seguinte
exibição na tela:
VERSÃO COM MATH.POW
"""
import math

contador = 0

while contador <= 15:
    print(f"3 elevado à {contador} é {math.pow(3,contador):.0f}")
    contador = contador + 1