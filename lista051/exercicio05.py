"""
5) Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser
impressa no seguinte formato:
"""

num = int(input("Digite um número:\n"))

contador = 1

while contador <= 10:
    print(f"{num} * {contador} = {num * contador}")
    contador = contador + 1
