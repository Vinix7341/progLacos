"""
4) Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ...
+ 97 + 98 + 99 + 100)
"""

contador = 1

soma = 0

while contador <= 100:
    soma = soma + contador
    contador = contador + 1

print(f"A soma dos cem primeiros números inteiros é {soma}")