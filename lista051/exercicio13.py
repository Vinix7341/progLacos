"""
13) Desenvolver um programa que imprima a tabuada de 3 a 6.
"""

tabu = 3
contador = 1
contador2 = 1

while contador <= 10:
    print(f"{tabu} * {contador} = {tabu * contador}")
    contador = contador + 1
    if contador == 11 and tabu < 6:
        contador = 1
        tabu = tabu + 1
